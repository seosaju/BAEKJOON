n = input()

int_n = int(n)
len_n = len(n)
if int_n - 9 * len_n < 0:
    start = 0
else:
    start = int_n - 9 * len_n

result = 0
for i in range(start, int_n):
    i_list = [int(a) for a in str(i)]
    if (i + sum(i_list)) == int_n:
        result = i
        break
print(result)
