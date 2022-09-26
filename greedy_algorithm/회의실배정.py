n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]
table.sort(key=lambda a: a[0])
table.sort(key=lambda a: a[1])

cnt = 1
end = table[0][1]
for i in range(1, n):
    if end <= table[i][0]:
        cnt += 1
        end = table[i][1]

print(cnt)
