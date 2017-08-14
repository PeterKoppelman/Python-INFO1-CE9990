"""
float2.py

Create an iterable class named float2.range.  Use it like this:

import float2

for f in float2.range(0.0, 1.0, 10)   #a sequence of 11 floats
    print(f)

The output is

0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
"""

import builtins

def range(start, end, n):
    "A generator function that yields a sequence of equally-spaced floats."

    if not isinstance(start, float) and not isinstance(start, int):
        raise TypeError("start must be float or int, not " + str(type(start)))
        
    # if not isinstance(end, float) and not isinstance(end, int):
    if not (isinstance(end, float) or isinstance(end, int)):
        raise TypeError("end must be float or int, not " + str(type(end)))
        # sys.exit(1)

    if not isinstance(n, int):
        # raise TypeError("n must be int, not " + str(type(n)))
        print ("n must be int, not " + str(type(n)))
        sys.exit(1)

    if n <= 0:
        # raise ValueError("n must be positive, not " + str(n))
        print ("n must be positive, not " + str(n))
        sys.exit(1)

    for i in builtins.range(n + 1):
        yield start + (end - start) * i / n


if __name__ == "__main__":
    import sys
    for f in range(0.0, 1.0, 10.0):
        print(f)
    sys.exit(0)
