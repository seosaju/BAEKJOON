x = int(input())
y = int(input())
z = int(input())
result = x * y * z
result_list = list(str(result))
result_dict = {}

for i in range(10):
    result_dict[i] = 0

for i in range(len(result_list)):
    if int(result_list[i]) in result_dict:
        result_dict[int(result_list[i])] += 1
    else:
        pass

for i in range(len(result_dict)):
    print(result_dict[i])
