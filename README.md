# Islamic Prayer Timings Script

A simple Python script that detects your approximate location using your public IP address and fetches Islamic prayer times based on local sunrise/sunset data. Built by **Ali Suheil** (GitHub: [@sailedship](https://github.com/sailedship)) and powered by [ipify.org](https://www.ipify.org/), [ipinfo.io](https://ipinfo.io/), and [sunrisesunset.io](https://sunrisesunset.io/).

---

## 📌 Features

- Auto-detects your city using your IP address.
- Asks for confirmation to ensure location accuracy.
- Fetches:
  - **Fajr** (dawn)
  - **Sunrise** (sunrise)
  - **Dhuhr** (solar noon)
  - **Asr** (Standard and Hanafi)
  - **Maghrib** (sunset)
  - **Isha** (dusk)
- Infinite loop for repeated usage without restarting.

---

## 🛠 Installation

pip install requests
pip install ipinfo
