string = input()
while len(string) > 10:
    print(string[:10])
    string = string[10:]
print(string)