import sys
import string
import math

x = sys.stdin.readline()

while x != "END":
    x = x.strip().split("=")
    ans = eval(x[0])
    gpt = x[1]
    if ans == int(gpt):
        print("ALL DATASETS WERE CORRECT")
    else:
        print("DIRECTIVE: {} != {}; CORRECT TO VALUE: {}".format(x[0], gpt, ans))
    x = sys.stdin.readline().strip()