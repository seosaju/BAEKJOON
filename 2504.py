stack = []
flag = True
for i in list(input()):
    if i in ['(', '[']:
        stack.append(i)
    else:
        try:
            pop = stack.pop()
        except IndexError:
            print(0)
            flag = False
            break
        temp = 0
        while pop != '[' and pop != '(':
            temp += pop
            try:
                pop = stack.pop()
            except IndexError:
                flag = False
                break
        if i == ')' and pop == '(':
            if temp == 0:
                stack.append(2)
            else:
                stack.append(2 * temp)
        elif i == ']' and pop == '[':
            if temp == 0:
                stack.append(3)
            else:
                stack.append(3 * temp)
        else:
            print('0')
            flag = False
            break

if flag:
    try:
        print(sum(stack))
    except TypeError:
        print(0)
