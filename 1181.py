import sys

words = list(set(sys.stdin.readline() for _ in range(int(sys.stdin.readline()))))
print(''.join(sorted(words, key=lambda x: (len(x), x))))
