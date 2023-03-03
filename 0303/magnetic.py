import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        stk = [2]
        for i in range(n):
            if arr[i][j] != 0:
                stk.append(arr[i][j])
                if stk[-1] == 2 and stk[-2] == 1:
                    cnt += 1
    print(f'#{tc} {cnt}')
