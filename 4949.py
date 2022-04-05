while True:
    text = input()

    if text == '.':
        break

    stack = []
    for t in text:
        if t in ["(", "["]:
            stack.append(t)
        elif t in ["]", ")"]:
            if len(stack) == 0:
                stack.append(t)
                break

            if (stack[-1] == "(" and t == ")") or (stack[-1] == "[" and t == "]"):
                stack.pop()
            else:
                stack.append(t)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
