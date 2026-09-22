
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

from crypto import encrypt_folder, decrypt_folder


# --------------------------------
# Lock Folder
# --------------------------------

def lock_folder():

    folder = filedialog.askdirectory(
        title="Select folder to lock"
    )

    if not folder:
        return

    password = simpledialog.askstring(
        "Create Password",
        "Enter a password:",
        show="*"
    )

    if not password:
        messagebox.showwarning(
            "Password Required",
            "Please enter a password."
        )
        return

    confirm_password = simpledialog.askstring(
        "Confirm Password",
        "Enter the password again:",
        show="*"
    )

    if not confirm_password:
        return

    if password != confirm_password:

        messagebox.showerror(
            "Password Mismatch",
            "❌ The passwords do not match."
        )
        return

    vault_path = folder + ".vault"

    if os.path.exists(vault_path):

        messagebox.showerror(
            "Already Exists",
            "A vault with this name already exists."
        )
        return

    try:

        encrypt_folder(
            folder,
            vault_path,
            password
        )

        messagebox.showinfo(
            "Success",
            f"🔒 Folder encrypted successfully!\n\n"
            f"Vault:\n{vault_path}"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Encryption failed:\n\n{e}"
        )


# --------------------------------
# Unlock Vault
# --------------------------------

def unlock_vault():

    vault = filedialog.askopenfilename(
        title="Select vault",
        filetypes=[
            ("CipherVault files", "*.vault"),
            ("All files", "*.*")
        ]
    )

    if not vault:
        return

    password = simpledialog.askstring(
        "Password",
        "Enter the vault password:",
        show="*"
    )

    if not password:
        return

    output_folder = filedialog.askdirectory(
        title="Select where to restore the folder"
    )

    if not output_folder:
        return

    folder_name = os.path.splitext(
        os.path.basename(vault)
    )[0]

    restore_path = os.path.join(
        output_folder,
        folder_name
    )

    if os.path.exists(restore_path):

        messagebox.showerror(
            "Already Exists",
            "The restore folder already exists."
        )
        return

    try:

        success = decrypt_folder(
            vault,
            restore_path,
            password
        )

        if success:

            messagebox.showinfo(
                "Success",
                f"🔓 Vault unlocked successfully!\n\n"
                f"Restored folder:\n{restore_path}"
            )

        else:

            messagebox.showerror(
                "Access Denied",
                "❌ Wrong password or corrupted vault."
            )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Decryption failed:\n\n{e}"
        )


# --------------------------------
# Main Window
# --------------------------------

root = tk.Tk()

root.title("CipherVault 🔐")
root.geometry("500x400")
root.resizable(False, False)


title = tk.Label(
    root,
    text="🔐 CipherVault",
    font=("Arial", 26, "bold")
)

title.pack(pady=(35, 5))


subtitle = tk.Label(
    root,
    text="Secure File & Folder Protection",
    font=("Arial", 12)
)

subtitle.pack(pady=(0, 35))


lock_button = tk.Button(
    root,
    text="🔒  Lock Folder",
    font=("Arial", 14),
    width=25,
    height=2,
    command=lock_folder
)

lock_button.pack(pady=10)


unlock_button = tk.Button(
    root,
    text="🔓  Unlock Vault",
    font=("Arial", 14),
    width=25,
    height=2,
    command=unlock_vault
)

unlock_button.pack(pady=10)


status = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 10)
)

status.pack(pady=30)


root.mainloop()

