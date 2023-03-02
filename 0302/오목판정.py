import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for di, dj in (1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1):
                    cnt = 1
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di
                        nj += dj
                        if cnt == 5:
                            ans = "YES"
                            break

    print(f'#{tc} {ans}')
