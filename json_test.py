"""
json_test.py

Download the current weather from OpenWeatherMap in JSON format.
"""

import sys
import urllib.request
import json
import time
import datetime

daysinmonth = [
    None,
    31, #January
    28, #February
    31, #March
    30, #April
    31, #May
    30, #June
    31, #July
    31, #August
    30, #September
    31, #October
    30, #November
    31  #December
]


def newtime(UTCtime):
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(UTCtime))
    return (localtime)


url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10025,US" \
    "&units=imperial" \
    "&mode=json" \
    "&APPID=532d313d6a9ec4ea93eb89696983e369"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

s = json.loads(s)
print(json.dumps(s, sort_keys=True, indent=4))
print()

# offset = (datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()
z = newtime(s['sys']['sunrise'])
print("sunrise = ", z)
print()

z = newtime(s['sys']['sunset'])
print("sunset = ", z)
print()

temperature = s['main']['temp']
if temperature == None:
    print("Couldn't find temperature.")
    sys.exit(1)

print("The temperature is {}°.".format(temperature))
sys.exit(0)
