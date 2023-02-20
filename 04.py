import sys
import string
import math

def truncate(number, digits):
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

x = sys.stdin.readline().split(" ")
y = float(x[0])
z = float(x[1])
total = 0

while y != 0 and z != 0:
    difference = z - y
    difference = truncate(difference, 1)
    total += difference
    txt = "DIFF: " + str(difference)
    print(txt.format(n = difference))
    x = sys.stdin.readline().rstrip().split(" ")
    y = float(x[0])
    z = float(x[1])

print("TOTAL:", str(truncate(total, 1)))