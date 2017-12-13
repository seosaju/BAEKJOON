n = []
exec(5 * "n.append(int(input())) ;")
for i in range(len(n)):
    if n[i] < 40:
        n[i] = 40
print(int(sum(n) / len(n)))
