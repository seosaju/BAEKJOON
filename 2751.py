import sys


def merge_sort(a):
    if len(a) <= 1:
        return a

    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
    return a


n = int(input())
x = [int(sys.stdin.readline()) for _ in range(n)]
x = merge_sort(x)
for result in x:
    print(result)
