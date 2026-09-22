import os
import zipfile
import base64

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


ITERATIONS = 600_000
SALT_SIZE = 16


def create_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )

    return base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )


def encrypt_folder(folder_path, vault_path, password):

    temp_zip = vault_path + ".tmp.zip"

    # Create ZIP
    with zipfile.ZipFile(
        temp_zip,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(folder_path):

            for filename in files:

                file_path = os.path.join(root, filename)

                archive_path = os.path.relpath(
                    file_path,
                    folder_path
                )

                zipf.write(
                    file_path,
                    archive_path
                )

    # Generate salt
    salt = os.urandom(SALT_SIZE)

    # Generate encryption key
    key = create_key(password, salt)

    cipher = Fernet(key)

    # Read ZIP
    with open(temp_zip, "rb") as file:
        data = file.read()

    # Encrypt
    encrypted_data = cipher.encrypt(data)

    # Save vault
    with open(vault_path, "wb") as file:
        file.write(salt)
        file.write(encrypted_data)

    # Delete temporary ZIP
    os.remove(temp_zip)


def decrypt_folder(vault_path, output_folder, password):

    temp_zip = vault_path + ".tmp.zip"

    # Read vault
    with open(vault_path, "rb") as file:
        data = file.read()

    salt = data[:SALT_SIZE]
    encrypted_data = data[SALT_SIZE:]

    # Generate key
    key = create_key(password, salt)

    cipher = Fernet(key)

    try:
        decrypted_data = cipher.decrypt(encrypted_data)

    except InvalidToken:
        return False

    # Save temporary ZIP
    with open(temp_zip, "wb") as file:
        file.write(decrypted_data)

    # Secure extraction
    output_path = os.path.abspath(output_folder)

    with zipfile.ZipFile(temp_zip, "r") as zipf:

        for member in zipf.infolist():

            member_path = os.path.abspath(
                os.path.join(
                    output_folder,
                    member.filename
                )
            )

            if not (
                member_path == output_path
                or member_path.startswith(
                    output_path + os.sep
                )
            ):
                os.remove(temp_zip)
                raise ValueError(
                    "Unsafe archive path detected"
                )

        zipf.extractall(output_folder)

    # Delete temporary ZIP
    os.remove(temp_zip)

    return True