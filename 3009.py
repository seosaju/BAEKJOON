x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_list = [x1, x2, x3]
x_set = set(x_list)
y_list = [y1, y2, y3]
y_set = set(y_list)

x_result = 0
y_result = 0
for x in x_set:
    if x_list.count(x) == 1:
        x_result = x

for y in y_set:
    if y_list.count(y) == 1:
        y_result = y

print(f'{x_result} {y_result}')
