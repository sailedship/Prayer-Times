#  DON'T REMOVE THIS TEXT! OTHER THAN THAT, DO WHATEVER YOU WANT!
import requests
import ipinfo
from datetime import datetime, timedelta

while True:
    current_date = datetime.now()
    day = current_date.weekday()

    print("\nIslamic Prayer Timings")
    print("By Ali Suheil, Powered by sunrisesunset.io and ipify.org\n")

    try:
        response = requests.get("https://api.ipify.org")
        ip_address = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error getting IP address: {e}")
        continue

    access_token = 'API KEY HERE, MAKE A FREE ACCOUNT'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)

    print(f"Detected city: {details.city}")
    boo = input("Is this city within 300 Kilometers or 200 miles of your current location? Type Y or N: ").upper()

    if boo == 'Y':
        print("Here are the prayer times for:", details.city)
    else:
        print("If you have a VPN on, turn it off and try again.")
        print("The program will now print the timings for", details.city)

    lat = float(details.latitude)
    long = float(details.longitude)

    try:
        url = f"https://api.sunrisesunset.io/json?lat={lat}&lng={long}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            results = data['results']
            fajr_str = results['dawn']
            isha_str = results['dusk']
            sunset_str = results['sunset']

            fajr_time = datetime.strptime(fajr_str, "%I:%M:%S %p") - timedelta(hours=1, minutes=11)
            isha_time = datetime.strptime(isha_str, "%I:%M:%S %p") + timedelta(hours=1, minutes=11)
            sunset_time = datetime.strptime(sunset_str, "%I:%M:%S %p")
            asr_hanafi = sunset_time - timedelta(hours=2, minutes=15)
            asr_standard = sunset_time - timedelta(hours=3, minutes=15)

            print("\nFajr:", fajr_time.strftime("%I:%M %p"))
            print("End of Fajr (Sunrise):", results['sunrise'])
            print("Dhuhr:", results['solar_noon'])
            print("Asr (Standard):", asr_standard.strftime("%I:%M %p"))
            print("Asr (Hanafi):", asr_hanafi.strftime("%I:%M %p"))
            print("Maghrib:", results['sunset'])
            print("Isha:", isha_time.strftime("%I:%M %p"))
        else:
            print("Error:", data.get("status", "Unknown error"))

    except requests.exceptions.RequestException as e:
        print(f"Error getting prayer times: {e}")

    input("\nPress ENTER to run again and pray for me.")
