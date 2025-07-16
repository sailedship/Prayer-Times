# Islamic Prayer Timings Script

A simple Python script that detects your approximate location using your public IP address and fetches Islamic prayer times based on local sunrise/sunset data. Built by **Ali Suheil** (GitHub: [@sailedship](https://github.com/sailedship)) and powered by [ipify.org](https://www.ipify.org/), [ipinfo.io](https://ipinfo.io/), and [sunrisesunset.io](https://sunrisesunset.io/).

---

## 📌 Features

- Auto-detects your city using your IP address.
- Asks for confirmation to ensure location accuracy.
- Calculates:
  - **Fajr** (dawn)
  - **Sunrise** (sunrise)
  - **Dhuhr** (solar noon)
  - **Asr** (Standard and Hanafi)
  - **Maghrib** (sunset)
  - **Isha** (dusk)
- Infinite loop for repeated usage without restarting.

---

## 🛠 Installation

- pip install requests

- pip install ipinfo

## OUTPUT:
Islamic Prayer Timings

By Ali Suheil, Powered by sunrisesunset.io and ipify.org


Detected city: Rawalpindi

Is this city within 300 Kilometers or 200 miles of your current location? Type Y or N: Y
Here are the prayer times for: Rawalpindi


Fajr: 4:41:54 AM

End of Fajr (Sunrise): 5:10:10 AM

Dhuhr: 12:14:56 PM

Asr (Standard): 04:04 PM

Asr (Hanafi): 05:04 PM

Maghrib: 7:19:41 PM

Isha : 7:47:57 PM

