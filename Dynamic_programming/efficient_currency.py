n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

best_case = [10001] * (m+1)

best_case[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if best_case[j - array[i]] != 10001:
            best_case[j] = min(best_case[j], best_case[j-array[i]] + 1)

if best_case[m] == 10001:
    print(-1)
else:
    print(best_case[m])
