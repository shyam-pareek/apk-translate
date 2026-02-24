<p align="center">
  <img src="docs/banner.svg" alt="APK-Translate Banner Dark"/>
</p>

# APK-Translate 🛡️
### Universal Android APK UI Translator for Security Testing

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Stars](https://img.shields.io/github/stars/shyam-pareek/apk-translate?style=social)
![Downloads](https://img.shields.io/github/downloads/shyam-pareek/apk-translate/total)
![Issues](https://img.shields.io/github/issues/shyam-pareek/apk-translate)
![Last Commit](https://img.shields.io/github/last-commit/shyam-pareek/apk-translate)

Translate localized Android app interfaces to English to streamline **mobile pentesting, API testing, and reverse engineering workflows**.

---

## 🧾 Overview

**APK-Translate** automates the process of translating non-English Android app UI strings into English.

It decompiles the APK, translates resources, rebuilds the app, and signs it - all in a single command.

Perfect for security researchers dealing with localized applications during assessments.

---

## 📚 Table of Contents

- Features
- How It Works
- Demo
- Prerequisites
- Installation
- Usage
- Output
- Project Structure
- Troubleshooting
- Contributing
- License
- Disclaimer

---

## 🚀 Features

- Automatic language detection  
- Batch translation across all resource folders  
- Special character escaping to prevent build failures  
- Fully automated pipeline  
- Works with any localized Android APK  

---

## ⚙️ How It Works

```
APK → Decompile → Extract strings → Detect language → Translate → Rebuild → Sign → Translated APK
```

---

## 📋 Prerequisites

- Python 3.x  
- Java JDK / JRE  
- Apktool - https://apktool.org/docs/install/  
- uber-apk-signer - https://github.com/patrickfav/uber-apk-signer/releases  

Place `uber-apk-signer.jar` in the project root.

---

## 🛠️ Installation

```bash
git clone https://github.com/shyam-pareek/apk-translate.git
cd apk-translate
pip install -r requirements.txt
```

---

## 💻 Usage

```bash
python3 translate_apk.py your_app.apk
```

Windows:

```bash
python translate_apk.py your_app.apk
```

---

## 📦 Output

```
your_app_translated.apk
```

The generated APK is signed and ready for installation.

---

## 📁 Project Structure

```
apk-translate/
│
├── translate_apk.py
├── requirements.txt
├── docs/
│   ├── banner.svg
│   └── logo.svg
└── README.md
```

---

## ⚠️ Troubleshooting

Check Apktool:

```bash
apktool -version
```

Check Java:

```bash
java -version
```

If build fails, ensure Java and Apktool are added to PATH.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repo  
2. Create a feature branch  
3. Commit changes  
4. Open a Pull Request  

---

## 📄 License

MIT License

---

## ❗ Disclaimer

For educational and authorized security testing only.  
The author is not responsible for misuse or damages.
