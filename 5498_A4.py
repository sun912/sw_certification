from collections import deque
import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int, str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op


def solve():
    dq = deque()
    dq.append(nums[0])
    cnt = 1
    for i in op:
        if i == '+':
            dq.append(nums[cnt])
            cnt += 1
        elif i == '-':
            dq.append(-nums[cnt])
            cnt += 1
        elif i == '*':
            result = dq.pop() * nums[cnt]
            dq.append(result)
            cnt += 1
        elif i == '/':
            result = int(dq.pop() / nums[cnt])
            dq.append(result)
            cnt += 1

    return sum(dq)


sol = -1
# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(sol)
