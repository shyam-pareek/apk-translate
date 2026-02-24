<p align="center">
  <img src="docs/banner.svg" alt="APK-Translate Banner Dark"/>
</p>

<p align="center">
  <img src="docs/logo.png" width="140" alt="APK-Translate logo"/>
</p>

# APK-Translate 🛡️
### High-Performance Android APK UI Translator for Security Testing

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Stars](https://img.shields.io/github/stars/shyam-pareek/apk-translate?style=social)
![Downloads](https://img.shields.io/github/downloads/shyam-pareek/apk-translate/total)
![Issues](https://img.shields.io/github/issues/shyam-pareek/apk-translate)
![Last Commit](https://img.shields.io/github/last-commit/shyam-pareek/apk-translate)

---

## 🧾 Overview

**apk-translate** is a high-performance Android APK UI translator designed for security researchers and penetration testers.

Unlike tools that rely on unreliable auto-detection, this tool uses **Strict Parameter Locking** and **Character-Range Validation** to ensure accurate translations of localized app strings.

It is especially useful during **mobile app pentesting and API security testing** where the backend is English but the UI is localized.

---

## 🚀 Key Features

- Strict parameter control (no language auto-guessing)  
- Character-range validation before translation  
- Real-time verbose translation feed  
- Progress tracking with percentage and string counters  
- Colorful terminal UI with clear status indicators  
- Fully automated workflow (Decompile → Translate → Rebuild → Sign)  
- Automatic escaping of problematic characters  

---

## 📊 Features & Output

This version provides high-level transparency during execution:

- **Live Percentage Tracking** — See progress per `strings.xml`
- **String Counter** — Total strings per resource folder
- **Execution Timer** — Full workflow runtime
- **Verbose Error Logs** — Clear diagnostics if a step fails

### Sample Output

```text
>>> [EXEC] Starting: Decompilation
>>> [SUCCESS] Decompilation completed.

[*] Analyzing: values-ja/strings.xml
[*] Total Strings found: 450
    Progress: [100%] (450/450)
[*] Finished file translation.

----------------------------------------
🏁 TRANSLATION SUMMARY
----------------------------------------
✅ Total Strings Translated: 1240
🕒 Total Time Elapsed: 3m 45s
📦 Final APK: app_translated.apk
----------------------------------------
```

---

## 🌈 Enhanced Terminal UI

- **Cyan [EXEC]** → System command running  
- **Green [SUCCESS]** → Step completed successfully  
- **Red [!!!]** → Critical error or missing dependency  
- **Live Progress Bar** → Real-time translation progress  

---

## 📋 Prerequisites

Ensure the following are installed and in PATH:

1. Python 3.x  
2. Java JRE/JDK  
3. Apktool — https://apktool.org/docs/install/  
4. uber-apk-signer — https://github.com/patrickfav/uber-apk-signer/releases  

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

### Command Syntax

```bash
# macOS / Linux
python3 apk-translate.py <file.apk> <lang_code>
```

---

## 📌 Common Examples

| Language | Code | Command |
|----------|------|--------|
| Japanese | `ja` | `python3 apk-translate.py app.apk ja` |
| Chinese | `zh` | `python3 apk-translate.py app.apk zh` |
| Korean | `ko` | `python3 apk-translate.py app.apk ko` |
| Hindi | `hi` | `python3 apk-translate.py app.apk hi` |
| Arabic | `ar` | `python3 apk-translate.py app.apk ar` |

---

## 🔍 How to Find Other Language Codes

The tool supports any **ISO 639-1 two-letter code**.

1. Visit  
   https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
2. Find your language  
3. Run:

```bash
python3 apk-translate.py app.apk el
```

Example: Greek → `el`, Turkish → `tr`

---

## 📦 Output

```
app_translated.apk
```

Signed APK ready for installation and testing.

---

## 📁 Project Structure

```
apk-translate/
│
├── apk-translate.py
├── requirements.txt
├── docs/
│   ├── banner.svg
│   └── logo.png
└── README.md
```

---

## 🛣️ Roadmap

- GUI interface  
- Bulk APK processing  
- Burp Suite integration  
- Plugin mode for reversing tools  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repo  
2. Create a branch  
3. Commit changes  
4. Open a Pull Request  

---

## 📄 License

MIT License

---

## ❗ Disclaimer

This project is intended for **educational and authorized security testing only**.  
The author is not responsible for misuse or damages.

---
