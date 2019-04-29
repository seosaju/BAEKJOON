import sys

n = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]
print(min(nums), max(nums))
