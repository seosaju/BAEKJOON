n = input().upper()
n_list = list()
for i in range(65, 91):
    n_list.append(n.count(chr(i)))
if n_list.count(max(n_list)) == 1:
    print(chr(ord('A') + n_list.index(max(n_list))))
else:
    print('?')
