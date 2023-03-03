import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for di, dj in (1,0),(-1,0),(0,1),(0,-1):
                ni, nj = i + di, j + dj
                for _ in range(arr[i][j]):
                    if 0<=ni<N and 0<=nj<M:
                        cnt += arr[ni][nj]
                        ni += di
                        nj += dj
            if cnt > ans:
                ans = cnt
    print(f'#{tc} {ans}')
