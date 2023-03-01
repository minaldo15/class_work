import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    N = 0
    for lst in arr:
        if len(lst) > N:
            N = len(lst)
    print(f'#{tc}', end=' ')
    for j in range(N):
        for i in range(5):
            if len(arr[i]) > j:
                print(arr[i][j], end='')
    print()