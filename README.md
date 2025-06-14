# 🕵️‍♂️ Browser Stealth Siphon (BSS)

**BSS - Browser Stealth Siphon** is a lightweight, open-source Python tool crafted for **research, forensic analysis, and offline browser data backup**. It extracts **saved passwords** (from older browser versions) and **browsing history** from Chromium-based browsers like Chrome, Edge, and Brave.

> ⚠️ This is a **clean, non-malicious version** of the script. All stealthy, encrypted, or automated exfiltration mechanisms have been removed. Intended only for **educational and research purposes**.

---

## ✨ Features

* 🔑 Extracts saved login credentials from local browser databases

  * Only works on **older formats** (`v10`) — **newer `v20` encryption is not supported**
* 🌐 Collects recent browsing history with timestamps
* 📃 Outputs structured `.txt` files for analysis
* 📦 Compresses all extracted data into a `.zip` archive (non-password protected)
* ✅ Compatible with:

  * Google Chrome
  * Microsoft Edge
  * Brave Browser

---

## 🛠 Requirements

* Windows OS
* Python 3.8+
* Python packages:

  ```bash
  pip install pycryptodome pytz
  ```

---

## 🚀 Usage

1. **Clone or download** this repository
2. **Run the script**:

   ```bash
   python bss_clean.py
   ```
3. **Output will be saved as**:

   ```
   extracted_data/
     ├── chrome_key20250614_123045.txt
     ├── chrome_log20250614_123045.txt
     ├── edge_key20250614_123045.txt
     ├── ...
     └── results_20250614_123045.zip
   ```

---

## 📁 Output Format

### Passwords file:

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

## 📃 License

Copyright (c) 2025 rahul-satapara

All rights reserved.

Permission is hereby granted to clone and use the software for educational or research purposes only.

Modification, or reverse engineering of any part of this software is strictly prohibited
without explicit written permission from the author.

This software is proprietary and protected by applicable copyright laws.
