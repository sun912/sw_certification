# https://www.acmicpc.net/problem/2839

import readline
from sys import stdin

readl = stdin.readline

n = int(readl())
count = 0


while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
