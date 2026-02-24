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
git clone [https://github.com/YOUR_USERNAME/apk-translate.git](https://github.com/YOUR_USERNAME/apk-translate.git)
cd apk-translate