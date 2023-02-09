import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for lst in arr:
        for i in range(8 - N + 1):
            if lst[i:i + N] == lst[i:i + N][::-1]:
                cnt += 1
    arr1 = list(zip(*arr))
    for lst in arr1:
        for i in range(8 - N + 1):
            if lst[i:i + N] == lst[i:i + N][::-1]:
                cnt += 1
    print(f'#{t} {cnt}')


