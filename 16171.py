x = input()
tmp = ''
for i in range(len(x)):
    if x[i].isalpha():
        tmp += x[i]
if input() in tmp:
    print(1)
else:
    print(0)
