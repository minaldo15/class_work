def msort(m):
    if len(m) == 1:
        return m
    left = []
    right = []
    middle = len(m)//2
    for x in range(m[0:middle+1]):
        left.append(m[x])
    for x in range(m[middle:]):
        right.append(m[x])

    left = msort(left)
    right = msort(right)
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    msort(arr)