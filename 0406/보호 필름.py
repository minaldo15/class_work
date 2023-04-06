import sys
sys.stdin = open('input.txt', 'r')

def check(lst):
    cnt = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            cnt += 1
            if cnt == 3:
                return 1
        else:
            cnt = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    arr1 = list(zip(*arr))
    change = 0
    while True:
        sm = 0
        for lst in arr1:
            sm += check(lst)
        if sm == W:
            ans = change
            break
        else:
            change += 1
            for i in range(D):
                pass




