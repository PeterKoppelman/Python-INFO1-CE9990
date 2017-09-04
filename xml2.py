"""
xml.py

Download the current weather from OpenWeatherMap in XML format.
"""

import sys
import urllib.request
import lxml.etree
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

def newtime(UTCtime, offset):
    # Recalcuate UTCtime to local time.
    # Strip out the "T" in the middle of the string
    UTCtime = str(UTCtime[:10])+" "+str(UTCtime[11:])
    # Change the string to a datetime and then get the number of
    # seconds since epoch
    epoch_UTC = datetime.datetime.\
                strptime(UTCtime, "%Y-%m-%d %H:%M:%S").timestamp()
    # Add/subtract the number of seconds that are the difference
    # between the UTC time and the local time
    TotalSecs = int(epoch_UTC + offset)
    # Chage seconds back to date format and change it to a string
    NewTime = str(datetime.datetime.fromtimestamp(TotalSecs))
    # Stick the "T" back in the middle of the string
    Updatedtime = NewTime[:10]+"T"+NewTime[11:]
    return(Updatedtime)

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

# offset = -5
offset = (datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()
offset= int(offset)
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
