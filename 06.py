import sys
import string
import math

x = sys.stdin.readline().strip("/n")
save = []
magic = 0

try:
    x = x.split(" ")
    xint = [int(s) for s in x]
    M = ((xint[0]**1+xint[1]**2)*((xint[2])**(1/2)/xint[3]))**(1/3)
    if M > magic:
        save = xint
    x = sys.stdin.readline().strip("/n")
except:
    print("{} Kindness, {} Stickers On Phone, {} Friends and {} Laughter produced the most Magic: {}".format(save[0], save[1], save[2], save[3], M))
    

