sets = set()
for _ in range(10):
    n = int(input())
    sets.add(n % 42)

print(len(sets))
