# https://www.acmicpc.net/problem/11047

from sys import stdin
readl = stdin.readline

n, k = map(int, readl().split())
currency = [int(readl()) for _ in range(n)]
# for _ in range(n):
#     currency.append(int(readl()))

count = 0
current = k

# while 로 더하기 연산을 하는것 보다 몫 연산으로 하는게 시간이 단축됨
# 전자의 방식으로 했을 때 시간초과 판정

for i in range(len(currency)-1, -1, -1):
    # print(i)
    # if currency[i] > k or current == k:
    #     break

    # while (current + currency[i]) <= k:
    #     current += currency[i]
    #     # print(current)
    #     count += 1
    #     if current == k:
    #         break
    count += current // currency[i]
    current = current % currency[i]

print(count)
