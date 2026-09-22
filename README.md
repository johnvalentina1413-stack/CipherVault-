# 🔐 CipherVault

**CipherVault** is a Python-based password-protected folder encryption vault designed to securely encrypt folders and restore them only when the correct password is provided.

This project was built as a cybersecurity learning project to understand practical concepts such as password-based key derivation, symmetric encryption, secure archive handling, and desktop application development.

## ✨ Features

* 🔒 Encrypt an entire folder into a `.vault` file
* 🔓 Decrypt and restore the original folder
* 🔑 Password-based encryption
* 🧂 Random salt generation for every vault
* 🛡️ PBKDF2-HMAC-SHA256 key derivation
* 🔐 Fernet authenticated encryption
* ❌ Wrong-password detection
* 🔁 Password confirmation when creating a vault
* 🛡️ ZIP path-traversal protection during extraction
* 🖥️ Simple desktop GUI built with Tkinter

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** — Graphical User Interface
* **Cryptography** — Encryption and key derivation
* **PBKDF2-HMAC-SHA256** — Password-based key derivation
* **Fernet** — Symmetric authenticated encryption
* **ZipFile** — Folder archiving

## 📂 Project Structure

```text
CipherVault/
│
├── app.py              # Tkinter graphical interface
├── crypto.py           # Encryption and decryption logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ How It Works

### 🔒 Lock a Folder

1. Open CipherVault.
2. Select **Lock Folder**.
3. Choose the folder you want to protect.
4. Enter a password.
5. Confirm the password.
6. CipherVault creates a `.vault` file containing the encrypted folder.

Conceptually:

```text
Folder
   ↓
ZIP Archive
   ↓
Random Salt
   ↓
PBKDF2-HMAC-SHA256
   ↓
Fernet Encryption
   ↓
Encrypted .vault
```

### 🔓 Unlock a Vault

1. Open CipherVault.
2. Select **Unlock Vault**.
3. Select the `.vault` file.
4. Enter the password.
5. Choose a restoration location.
6. CipherVault decrypts and restores the folder.

```text
Encrypted .vault
       ↓
Password
       ↓
PBKDF2-HMAC-SHA256
       ↓
Fernet Decryption
       ↓
ZIP Archive
       ↓
Restored Folder
```

## 🔐 Security Design

CipherVault does not store the user's password.

Instead, the password is used with a randomly generated salt to derive an encryption key using **PBKDF2-HMAC-SHA256**.

The current implementation uses:

```text
Algorithm: PBKDF2-HMAC-SHA256
Iterations: 600,000
Salt: 16 bytes
Derived Key: 32 bytes
Encryption: Fernet
```

The salt is stored with the encrypted vault so that the same password can derive the correct key during decryption.

## 🛡️ Secure Archive Extraction

CipherVault validates archive paths before extraction to help prevent **ZIP path traversal (Zip Slip)** attacks.

Archive entries are checked to ensure that extraction remains inside the intended destination directory.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/CipherVault.git
```

Move into the project directory:

```bash
cd CipherVault
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## 🧪 Testing

For safety, test CipherVault using dummy folders and files before using important personal data.

Example:

```text
test_folder/
├── document.txt
├── notes.txt
└── sample/
    └── example.txt
```

Do not upload test folders, encrypted vaults, passwords, or private files to the repository.

## ⚠️ Current Version

**CipherVault V1** is an encryption-vault prototype.

The current version creates an encrypted `.vault` copy while leaving the original folder unchanged. This behavior is intentional during development to reduce the risk of accidental data loss.

Future versions will explore a more integrated file/folder protection workflow.

## 🔮 Future Improvements

Planned improvements include:

* [ ] Windows Explorer integration
* [ ] Password-protected file/folder access workflow
* [ ] Improved vault management
* [ ] Automatic integrity verification
* [ ] Better handling of large files
* [ ] Improved GUI and status indicators
* [ ] Secure recovery-key mechanism
* [ ] Application packaging as a Windows `.exe`
* [ ] Security logging and audit events

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

* Symmetric cryptography
* Password-based key derivation
* Salt generation
* Secure archive handling
* Authentication and integrity protection
* Path traversal prevention
* Python GUI development
* Basic secure software design

## 👩‍💻 Author

**Valentina John**

BSc Information Technology student with an interest in **Cybersecurity, Network Security, and Security Engineering**.

This project was created as part of my hands-on cybersecurity learning and portfolio development.

## 📜 Disclaimer

CipherVault is an educational cybersecurity project and should be thoroughly tested and reviewed before being used to protect highly sensitive or irreplaceable data.

Always maintain a secure backup of important files.

---

⭐ If you find this project useful, feel free to explore the repository and follow its development.
