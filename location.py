"""
location.py

Peter Koppelman August 14, 2017
"""

import urllib.request
import json
import sys

class Location(object):
    """
    Class Location demonstrates class and instance attributes, class and instance methods.
    """

    def __init__(self, latitude, longitude):
        if not (isinstance(latitude, int) or isinstance(latitude, float)):
            raise TypeError("Latitude must be an integer or a float")
        if not (isinstance(longitude, int) or isinstance(longitude, float)):
            raise TypeError("Longitude must be an integer or a float")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude mst be between -90 and 90")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")

        self.latitude = latitude
        self.longitude = longitude

    #These two methods are getters.

    def getLatitude(self):
        "Return latitude."
        return self.latitude

    def getLongitude(self):
        "Return longitude"
        return self.longitude
    
    def setLatitude(self, latitude):
        "Return latitude."
        self.latitude = latitude
        return self.latitude

    def setLongitude(self, longitude):
        "Return longitude"
        self.longitude = longitude
        return self.longitude
    

    def __str__(self):
        "Return a string that looks like the contents of myself."
        degSym = "\u00b0"
        # Get the directions (North, East, South and West)
        latDir = ("N" if self.latitude >= 0 else "S")
        longDir = ("E" if self.longitude >= 0 else "W")
        # Clean up leading zeros
        newLatitude = str(self.latitude).lstrip("0")
        newLongitude = str(self.longitude).lstrip("0")
        # return "{:09}{}{}/{:09}{}{}".format(self.latitude, degSym, latDir, self.longitude, degSym, longDir)
        return "{}{}{}/{}{}{}".format(newLatitude, degSym, latDir, newLongitude, degSym, longDir)

    def getZipcode(self):
        "Returns zipcode"
        
        # url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40.7541476,-73.9818586"
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(self.latitude,self.longitude)
        
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

        try:
            dictionary = json.loads(s)          #dictionary is a dictionary.
        except json.JSONDecodeError as jSONDecodeError:
            print(jSONDecodeError)
            sys.exit(1)

        results = dictionary["results"]                        #results is a list of dictionaries
        if len(results) == 0:
            return 0

        firstResult = results[0]                               #firstResult is a dictionary
        address_components = firstResult["address_components"] #address_components is a list of dictionaries

        for component in address_components:                   #component is a dictionary
            if "postal_code" in component["types"]:            #component["types"] is a list of strings
                return int(component["long_name"])             #component["long_name"] is a string that looks like a zipcode

        return 0

    #The definition of classlocation ends here.


# if __name__ == "__main__":
    # import sys
    # import urllib.request
    # import json
    # A sample latitude and longitude
    # latitude = 40.785091
    # longitude = -73.9818586
    # x = Location(latitude, longitude)
    # y = 
    # print("Location is ", x)
    # print("Zipcode is",
    
    # sys.exit(0)
