"""
xml.py

Download the current weather from OpenWeatherMap in XML format.
"""

import sys
import urllib.request
import lxml.etree

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

def newtime(UTCtime, offset):

    year = int(UTCtime[0:4])
    month = int(UTCtime[5:7])
    day = int(UTCtime[8:10])
    hour = int(UTCtime[11:13])
    minute = UTCtime[14:16]
    seconds = UTCtime[17:]

    # check for previous day
    if hour <= abs(offset) and offset < 0:       
        hour = hour + 24 + offset
        # if day = 1, decrement month and make day the last day of previous month
        if day == 1:
            month = month - 1 if month != 1 else 12
            # if leap year and month = 2 day = 29 else last day in month.
            day = 29 if year%4 == 0 and month == 2 else daysinmonth[month]
            # if month = 12 decrement year
            year = year if month != 12 else year - 1
        else:
            day = day - 1
    # check for next day
    elif offset > 0 and hour + offset >= 24: 
        if day == daysinmonth[month]:
            # Check for leap year
            month = month if year%4 == 0 and month == 2 else month + 1
            # if leap year and month = 2 day = 29 else day = 1
            day = 29 if year%4 == 0 and month == 2 else 1
            if month == 13:
                month = 1
                year = year + 1
    # same day, just increment or decrement hours
    else:
        hour = hour + offset

    # pad fields with a 0 where needed and change integers to strings
    hour = str(hour) if hour >= 10 else "0"+str(hour)
    day = str(day) if day >= 10 else "0"+str(day)
    month = str(month) if month >= 10 else "0"+str(month)
    updatedTime = str(year)+"-"+ month+"-"+day+"T"+hour+":"+ minute+":"+seconds
    return (updatedTime)


url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10025,US" \
    "&units=imperial" \
    "&mode=xml" \
    "&APPID=532d313d6a9ec4ea93eb89696983e369"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

#Create an XML tree and pretty print it.
try:
    root = lxml.etree.fromstring(sequenceOfBytes)
except lxml.etree.XMLSyntaxError as error:
    print(error)
    sys.exit(1)

prettySequenceOfBytes = lxml.etree.tostring(root, pretty_print = True)

try:
    prettyS = prettySequenceOfBytes.decode("utf-8")   #prettyS is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)
    
print(prettyS)
print()

offset = -5
sun = root[0][2]
sun_rise = sun.get("rise")
z = newtime(sun_rise, offset)
print("Eastern std time sun rise ", z)
sun.set("rise", z)
value = sun.get("rise")
print("Sun rise in XML = {} ".format(value))
print()

sun_set = sun.get("set")
z = newtime(sun_set, offset)
print("Eastern std time sun set ", z)
sun.set("set", z)
value = sun.get("set")
print("Sun set in XML = {} ".format(value))
print()

element = root.find("lastupdate")
temp = element.get("value")
z = newtime(temp, offset)
print("Eastern std time last update ", z)
element.set("lastupdate", z)
value = element.get("lastupdate")
print("last update in XML = {} ".format(value))
#Print the current temperature.

temperature = root.find("temperature")
if temperature == None:
    print("Couldn't find temperature.")
    sys.exit(1)

value = temperature.get("value")
if value == None:
    print("Couldn't find value of temperature.")
    sys.exit(1)

unit = temperature.get("unit")
if unit == None:
    print("Couldn't find unit of temperature.")
    sys.exit(1)
print()
print("The temperature is {}° {}.".format(value, unit))
sys.exit(0)
