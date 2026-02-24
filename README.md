# apk-translate 🛡️

**apk-translate** is a universal Android APK UI translator designed for security researchers and penetration testers. It automatically detects and converts non-English app strings (Japanese, Chinese, Arabic, Hindi, etc.) into English. 

This tool is specifically helpful when performing **API Security Testing** on apps where the backend is in English, but the UI is localized in a foreign language.

---

## 🚀 Features
* **Universal Detection:** Automatically identifies the source language.
* **Batch Translation:** Scans all resource folders (`values`, `values-ja`, etc.).
* **Auto-Fixing:** Automatically escapes special characters (apostrophes, quotes) that usually break Apktool builds.
* **One-Click Workflow:** Decompiles, translates, rebuilds, and signs the APK in one go.

---

## 📋 Prerequisites

Before running the script, ensure you have the following installed:

1.  **Python 3.x**
2.  **Java JRE/JDK** (Required for Apktool and Signing)
3.  **Apktool**: [Installation Guide](https://apktool.org/docs/install/)
4.  **uber-apk-signer.jar**: [Download latest release](https://github.com/patrickfav/uber-apk-signer/releases) (Place it in the same folder as the script).

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/shyam-pareek/apk-translate.git
```
cd apk-translate

2. Install Python Dependencies
Ensure you have Python 3 installed, then run:

Bash
```
pip install -r requirements.txt
```
💻 How to Use

Step 1: Prepare your files
Place the APK you want to translate and the uber-apk-signer.jar file inside the apk-translate folder.

Step 2: Run the script

On macOS / Linux:
```python3 translate_apk.py your_app.apk```

On Windows:
```python translate_apk.py your_app.apk```

The script will perform the following automatically:

**Decompile**: Extracts the APK resources using Apktool.

**Translate**: Scans all strings.xml files, detects foreign languages, and translates them to English.

**Rebuild**: Recompiles the resources into a new APK.

**Sign**: Signs the APK using uber-apk-signer so it is ready for installation.

The final version will be saved as: your_app_translated.apk.

⚠️ **Troubleshooting**
**Apktool Errors**: Ensure apktool is in your System PATH. Check by typing apktool -version.

**Java Errors**: Ensure Java is installed. The script needs it to rebuild and sign the APK.

**Apostrophe Errors**: This script automatically handles (escapes) apostrophes and special characters that often break the apktool build process.

⚖️ **License & Disclaimer**
Distributed under the MIT License.

**Disclaimer:** This tool is intended for educational purposes and authorized security testing only. The author is not responsible for any misuse or damage caused by this tool.
