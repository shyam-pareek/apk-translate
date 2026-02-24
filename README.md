# apk-translate 🛡️

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/shyam-pareek/apk-translate?style=social)

**apk-translate** is a universal Android APK UI translator designed for security researchers and penetration testers. It automatically detects and converts non-English app strings (Japanese, Chinese, Arabic, Hindi, etc.) into English.

This tool is specifically helpful when performing **API Security Testing** on apps where the backend is in English, but the UI is localized in a foreign language.

---

## 🧾 Short Description (GitHub Sidebar)

Universal APK UI translator that converts localized Android app strings to English to simplify security testing and reverse engineering workflows.

---

## 🚀 Features

- **Universal Detection:** Automatically identifies the source language  
- **Batch Translation:** Scans all resource folders (`values`, `values-ja`, etc.)  
- **Auto-Fixing:** Escapes special characters that usually break Apktool builds  
- **One-Click Workflow:** Decompile → Translate → Rebuild → Sign  

---

## 🎬 Demo

> Replace the path below after uploading your GIF (example: `/docs/demo.gif`)

![apk-translate demo](docs/demo.gif)

---

## 📋 Prerequisites

1. **Python 3.x**  
2. **Java JRE/JDK** (Required for Apktool and signing)  
3. **Apktool** – https://apktool.org/docs/install/  
4. **uber-apk-signer.jar** – https://github.com/patrickfav/uber-apk-signer/releases  
   - Place it in the same folder as the script  

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shyam-pareek/apk-translate.git
cd apk-translate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Step 1 — Prepare Files

Place your target APK and `uber-apk-signer.jar` inside the project folder.

### Step 2 — Run

**macOS / Linux**

```bash
python3 translate_apk.py your_app.apk
```

**Windows**

```bash
python translate_apk.py your_app.apk
```

---

## 🔄 Workflow

1. **Decompile** → Extracts resources with Apktool  
2. **Translate** → Converts all detected non-English strings  
3. **Rebuild** → Compiles the modified resources  
4. **Sign** → Produces an installable APK  

Output file:

```
your_app_translated.apk
```

---

## ⚠️ Troubleshooting

**Check Apktool**

```bash
apktool -version
```

**Check Java**

```bash
java -version
```

**Build Errors**

The script auto-escapes problematic characters like apostrophes and quotes.

---

## ⚖️ License

MIT License

---

## ❗ Disclaimer

This tool is intended for **educational purposes and authorized security testing only**.  
The author is not responsible for misuse or damage caused by this tool.
