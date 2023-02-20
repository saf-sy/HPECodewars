import math
import sys

E = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
N = E * M
print(N, "\nToo Many Bugs! Abandon Game!!" if N > 500000 else "")