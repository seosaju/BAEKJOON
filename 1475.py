n = input().count
print(max([n(i) for i in "01234578"] + [(n('6') + n('9') + 1) // 2]))
