#!/usr/bin python2

import argparse
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="Name of the city to display the weather details.")
    parser.add_argument("-d", "--delay", help="Set the delay for notifications in seconds. By default, it is 60 seconds", type=int, default=60)
    args = parser.parse_args()

    url = "http://api.openweathermap.org/data/2.5/weather?q=" + args.city + "&mode=xml&units=metric"

    while True:
        r = requests.get(url, timeout=5)

        while r.status_code is not requests.codes.ok:
                r = requests.get(url, timeout=5)
    
        soup = BeautifulSoup(r.text)
        data = ("City: " + soup.city["name"] + ", Country: " + soup.country.text + "\nTemperature: " + soup.temperature["value"] +
        " Celsius\nWind: " + soup.speed["name"] + ", Direction: " + soup.direction["name"] + "\n\n" + soup.weather["value"])

        #print data

        sendmessage("Today\'s weather", data)
        sleep(args.delay)

if __name__ == "__main__":
    main()
