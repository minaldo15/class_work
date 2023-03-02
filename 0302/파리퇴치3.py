import sys
sys.stdin = open('input.txt', 'r')

di = [1, 0, -1, 0, -1, -1, 1, 1]
dj = [0, 1, 0, -1, -1, 1, -1, 1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N):
        for j in range(N):
            plus = arr[i][j]
            multi = arr[i][j]
            ci, cj = i, j
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                for _ in range(M-1):
                    if 0 <= ni < N and 0 <= nj < N:
                        plus += arr[ni][nj]
                        ni += di[d]
                        nj += dj[d]
            for d in range(4, 8):
                ni, nj = ci + di[d], cj + dj[d]
                for _ in range(M - 1):
                    if 0 <= ni < N and 0 <= nj < N:
                        multi += arr[ni][nj]
                        ni += di[d]
                        nj += dj[d]
            if plus > max:
                max = plus
            if multi > max:
                max = multi
    print(f'#{tc} {max}')
