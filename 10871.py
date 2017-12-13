_, min_num = map(int, input().split())
print(" ".join([str(n) for n in map(int, input().split()) if n < min_num]))
