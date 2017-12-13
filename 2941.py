cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input()
result = len(x)
for i in cro:
    result -= x.count(i)
print(result)
