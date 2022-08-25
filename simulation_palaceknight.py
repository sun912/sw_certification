
input_data = input()
row = int(input_data[1])

# 문자를 숫자로 바꾸는 과정
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, 1), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[1]
    next_col = col + step[0]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
