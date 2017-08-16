"""
uselocation.py

Create and use an object of class Location imported from module location.
"""

import sys
import location  #This is the location.py file you have to write.

def display(loc):
    assert isinstance(loc, location.Location)
    print("The latitude of {} is {}.".format(loc, loc.getLatitude()))
    print("The longitude of {} is {}.".format(loc, loc.getLongitude()))
    print("The zipcode of {} is {}.".format(loc, loc.getZipcode()))
    print()

loc = location.Location(40.7541476, -73.9818586)   #11 West 42nd Street
display(loc)

# Boston commons - check to see if format of zip code works with a leading 0
loc.setLatitude(42.3550)
loc.setLongitude(-71.0655)
display(loc)

#Go up to Yonkers.
loc.setLatitude(40.921787)
loc.setLongitude(-73.905614)
display(loc)

#Go to the North Pole.  Longitude there is irrelevant.
loc.setLatitude(90)
display(loc)

sys.exit(0)
