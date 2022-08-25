# 문제 5499 Building2

from collections import deque
import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height


sol_list = []
N, height = Input_Data()





print(*sol_list, sep='\n')
