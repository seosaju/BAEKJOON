old_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_c = "22233344455566677778889999"
s = input()
print(eval("+".join(s.translate(s.maketrans(old_c, new_c)))+"+len(s)"))
