"""
location.py

PEter Koppelman August 14, 2017
"""

import urllib.request
import json
import sys

class Location(object):
    """
    Class Location demonstrates class and instance attributes, class and instance methods.
    It is a simple date class, containing year, month, and day integers.
    """

  
    def __init__(self, latitude, longitude):
        if not (isinstance(latitude, int) or isinstance(longitude, float)):
            raise TypeError("Latitude must be and integer or a float")
        if not (isinstance(longitude, int) or isinstance(longitude, float)):
            raise TypeError("Longitude must be and integer or a float")
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
        return self.latitude

    def setLongitude(self, longitude):
        "Return longitude"
        return self.longitude
    

    def __str__(self):
        "Return a string that looks like the contents of myself."
        if self.latitude > 0:
            latDir = "N"
        else:
            latDir = "S"
        if self.longitude > 0:
            longDir = "E"
        else:
            longDir = "W"
            
        return "{:09}{}/{:09}{}".format(self.latitude, latDir, self.longitude, longDir)

    def getZipcode(self):
        "Returns zipcode"
        print(self.latitude)
        print(self.longitude)
        
        # url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40.7541476,-73.9818586"
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=self.latitude,self.longitude"

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
    # import datetime
    # now = datetime.datetime.now()
    #Create a Date object holding today's date.
    # d = Date(now.month, now.day, now.year)
    # print("Today is ", d, ".", sep = "")
    # sys.exit(0)
