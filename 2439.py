n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

"""
n = int(input())
for i in range(1, n + 1):
    print("{:>5}".format("*" * i))
얘는 왜 안되는거지?
"""