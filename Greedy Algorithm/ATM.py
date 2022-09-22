n = int(input())
array = list(map(int, input().split()))
result = 0

array.sort()
for i in range(1, n+1):
    result += sum(array[0:i])
print(result)
