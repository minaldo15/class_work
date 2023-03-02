import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = []
    N = 0
    for _ in range(5):
        lst = list(input())
        arr.append(lst)
        if len(lst) > N:
            N = len(lst)
    print(f'#{tc}', end=' ')
    for j in range(N):
        for i in range(5):
            if j < len(arr[i]):
                print(arr[i][j], end = '')
    print()