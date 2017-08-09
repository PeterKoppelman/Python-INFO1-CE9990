"""
classDate.py

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its instance methods.
"""

import sys

class Date(object):
    """
    Class Date demonstrates class and instance attributes, class and instance methods.
    It is a simple date class, containing year, month, and day integers.
    """

    lengths = [
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

    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12

    def __init__(self, month, day, year):
        assert isinstance(year, int)
        # assert isinstance(month, int) and 1 <= month and month <= 12
        assert isinstance(month, int) and 1 <= month and month <= Date.monthsInYear()
        assert isinstance(day, int) and 1 <= day and day <= Date.lengths[month]
        self.year = year
        self.month = month
        self.day = day

    #These three methods are getters.

    def getYear(self):
        "Return my year."
        return self.year

    def getMonth(self):
        "Return the number of my month (1 to 12 inclusive)."
        return self.month

    def getDay(self):
        "Return the number of my day (1 to the length of my month, inclusive)."
        return self.day

    def __str__(self):
        "Return a string that looks like the contents of myself."
        return "{:02}/{:02}/{:04}".format(self.month, self.day, self.year)

    def dayOfYear(self):
        "Return my day of the year: a number in the range 1 to 365 inclusive."
        return sum(Date.lengths[1:self.month]) + self.day

    def nextDay(self):
        "Move myself one day into the future."
        if self.day < Date.lengths[self.month]:
            self.day += 1
        else:
            self.day = 1       #Go to the first day of the next month.
            # if self.month < len(Date.lengths) - 1:
            if self.month < Date.monthsInYear():
                self.month += 1
            else:
                self.month = 1 #Go to the first month of the next year.
                self.year += 1

    def nextDays(self, n):
        "Move myself n days into the future."
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.nextDay()     #Call the instance method in line 62.

    @staticmethod
    def monthsInYear():
        "Return the number of months in a year.  This function is selfless."
        return len(Date.lengths) - 1;

    @staticmethod
    def daysInYear():
        "Returns the number of days in a year"
        return sum(d.lengths[1:])

    # Item 6
    def prevDay(self):
        if self.day != 1:
            self.day -= 1
        else:
            if self.month != 1:
                self.day = Date.lengths[self.month - 1]
                self.month -= 1
            else:                       #Special case for January 1
                self.day = Date.lengths[12]
                self.month = 12
                self.year -= 1

    # Item 6            
    def prevDays(self, n):
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.prevDay()

    # Item 7
    def __sub__(self, other):
        """
        Return the distance in days between the two Date objects.
        The return value is positive is self is later than other,
        negative if self is earlier than other, and zero if they're the same Date.
        """
        iself  = 365 *  self.year +  self.dayOfYear()
        iother = 365 * other.year + other.dayOfYear()
        return iself - iother

    # Item 8
    def __lt__(self, other):
        "Return True if self is earlier than the other Date, False otherwise."
        return self - other < 0   #means return __sub__(self, other) < 0
    
    #The definition of class Date ends here.


print("months in year =", Date.monthsInYear())
# d = Date(12, 31, 2017)         #Call the instance method in line 32.
d = Date(Date.december, 31, 2017)
print("months in year =", d.monthsInYear())
print("type(d) =", type(d))
print()

#These three statements do the same thing:
print("d =", d)
print("d =", str(d))
print("d =", d.__str__())      #Call the instance method in line 54.
print()

print("month =", d.getMonth()) #Call the instance method in line 46.
# print("month =", d.month)
print("day =", d.getDay())     #Call the instance method in line 50.
print("year =", d.getYear())   #Call the instance method in line 42.
print()

print("days in a year = ", d.daysInYear())

# p = d
# Previous Date information
p = Date(Date.january, 3, 2017)
print("p =", p)
p.prevDay()
print(p, "is the previous day.")
p.prevDays(7)
print(p, "is a week before that.")
print()

# Day of the year and next date.
print("{} is day number {} of the year {}.".format(d, d.dayOfYear(), d.getYear()))
d.nextDay()                    #Call the instance method in line 62.
print(d, "is the next day.")
d.nextDays(7)                  #Call the instance method in line 74.
print(d, "is a week after that.")
print()

# Item 7 - subtraction
d = Date(Date.december, 31, 2018)
e = Date(Date.december, 31, 2017)
print("d = ",d)
print("e = ",e)
print("Difference in dates is",d - e)   #means print(__sub__(d, e))

# Item 8
if e < d:   #means if __lt__(e, d):
    print(e, " is earlier than ", d, ".", sep = "")
else:
    print(e, " is equal to or later than ", d, ".", sep = "")


sys.exit(0)
