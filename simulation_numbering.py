input_data = sorted(list(input()))
# print(input_data)
sum = 0
# for i in range(len(input_data)):
#     if input_data[i] < 'A':
#         sum += int(input_data[i])
#         # input_data.remove(input_data[i])
#     else:
#         index = i
#         break

# result = input_data[i:]

# print(''.join(result) + str(sum))

result = []

for x in input_data:
    if x.isalpha():
        result.append(x)
    else:
        sum += int(x)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))
