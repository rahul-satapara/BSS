# 🕵️‍♂️ Browser Stealth Siphon (BSS)

**BSS - Browser Stealth Siphon** is a lightweight, open-source Python tool crafted for **research, forensic analysis, and offline browser data backup**. It extracts **saved passwords** (from older browser versions) and **browsing history** from Chromium-based browsers like Chrome, Edge, and Brave.

> ⚠️ This is a **clean, non-malicious version** of the script. All stealthy, encrypted, or automated exfiltration mechanisms have been removed. Intended only for **educational and research purposes**.

---

## ✨ Features

- 🔐 Extracts saved passwords from local databases (only for legacy formats using `v10` encryption)
- 🌍 Collects browser history with visited and searched URLs
- 📄 Saves data into easy-to-read `.txt` files
- 🗜️ Compresses all results into a `.zip` archive named `results_<timestamp>.zip`
- 🧹 Automatically deletes temporary folders after zipping
- 💡 Supports:
  - Google Chrome
  - Microsoft Edge
  - Brave Browser

---

## 📦 Requirements

- Windows OS (with Chromium-based browsers installed)
- Python 3.8 or higher
- Install required libraries:
  ```bash
  pip install pycryptodome pytz pypiwin32
  ```

---

## 🚀 Usage

### 🧪 For Python:
```bash
python 'BSS v1.py'
```

### ⚙️ For Executable (Optional):
Convert the script to a standalone `.exe` using PyInstaller:
```bash
pyinstaller --onefile --noconsole 'BSS v1.py'
```

### 📂 Output:
```
results_20250614_153045.zip
```
The zip will contain files like:
```
chrome_passwords_20250614_153045.txt
chrome_history_20250614_153045.txt
...
```

---

## 📁 File Format

### Passwords
```
[Site] https://example.com
[Username] user@example.com
[Password] hunter2
```

### History file:

```
[Visited] | 2025-06-14 12:30:45 | https://example.com | example.com
[Search]  | 2025-06-14 12:28:10 | how to zip a file | google.com
```

---

## ⚖️ Legal & Ethical Usage

This tool is for:

* 🧪 **Educational and ethical research**
* 🕵️ **DFIR (Digital Forensics and Incident Response)**
* 💾 **Personal offline backup of browser data**
* 🔒 **Testing and improving browser security**

> ❌ **Do NOT use this tool on devices or user profiles without explicit permission.**
> The author(s) take **no responsibility** for any misuse of this code.

---

## 🧾 License

This project is licensed under the **MIT License**. See the `LICENSE` file for full details.

You're welcome to fork and build on it. Always act **ethically** and **legally**.

---

## 🤝 Contributions

We welcome contributions! If you have an idea for a new feature or improvement:
1. Fork the repo
2. Create a new branch
3. Submit a Pull Request (PR)

> All contributions will be reviewed before merging.

---

## ⚠️ Disclaimer

> ❌ **Never run this tool on machines or user profiles you do not own or have explicit permission to analyze.**
> 
> The developers are not responsible for any misuse.

---

Made with ❤️ for DFIR, learning, and ethical hacking.
