import sys

n = int(sys.stdin.readline())
member = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    member.append((age, name))

member.sort(key=lambda x: (len(x[0]), x[0]))
for i in range(n):
    print(member[i][0], member[i][1])
