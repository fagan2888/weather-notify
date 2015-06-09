#!/usr/bin python2

import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

def Main():

    url = "http://api.openweathermap.org/data/2.5/weather?q=agra&mode=xml&units=metric"

    while True:
        r = requests.get(url, timeout=5)

        while r.status_code is not requests.codes.ok:
                r = requests.get(url, timeout=5)
    
        soup = BeautifulSoup(r.text)
        data = ("City: " + soup.city["name"] + ", Country: " + soup.country.text + "\nTemperature: " + soup.temperature["value"] +
        " Celsius\nWind: " + soup.speed["name"] + ", Direction: " + soup.direction["name"] + "\n\n" + soup.weather["value"])

        #print data

        sendmessage("Today\'s weather", data)
        sleep(60)

if __name__ == "__main__":
    Main()
