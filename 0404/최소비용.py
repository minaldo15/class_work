import sys
sys.stdin = open('input.txt','r')

def bfs(i, j):
    q = [(i,j)]
    v[i][j] = 0
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[ci][cj] + 1 + max(0, arr[ni][nj] - arr[ci][cj]):   # 다음 위치가 INF라면
                v[ni][nj] = v[ci][cj] + 1 + max(0, arr[ni][nj] - arr[ci][cj])
                q.append((ni,nj))
    return v[-1][-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = N * N * 1000
    v = [[INF]*N for _ in range(N)]
    ans = bfs(0, 0)
    print(f'#{tc} {ans}')
