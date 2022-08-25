'''
    def finding_length(input_list, target: int, start: int, end: int) -> int:
        mid = (start + end) // 2
        # result = sum(list(input_list[:] - mid))
        search_result = [input_list[i] - input_list[mid] if (input_list[i] -
                        input_list[mid]) >= 0 else 0 for i in range(len(input_list))]
        result = sum(search_result)

        if result == target:
            return input_list[mid]
        elif result > target:
            return finding_length(input_list, target, mid+1, end)
        else:
        return finding_length(input_list, target, start, mid-1)
'''
# input_list.sort()
# print(finding_length(input_list, m, 0, n-1))

n, m = map(int, input().split())
input_list = list(map(int, input().split()))

start = 0
end = max(input_list)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in input_list:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
