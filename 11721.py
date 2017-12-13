string = input()
while string.__len__() > 10:
    print(string[:10])
    string = string[10:]
print(string)