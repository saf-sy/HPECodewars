import sys
import string
import math

x = sys.stdin.readline().rstrip().strip()
save = []
magic = 0

while x != "0":
    x = x.split(" ")
    xint = [int(s) for s in x]
    M = ((xint[0]**1+xint[1]**2)*((xint[2])**(1/2)/xint[3]))**(1/3)
    if M > magic:
        save = x
        magic = M
    x = sys.stdin.readline().strip()
    
print("{} Kindness, {} Stickers On Phone, {} Friends and {} Laughter produced the most Magic: {}".format(save[0], save[1], save[2], save[3], magic))
