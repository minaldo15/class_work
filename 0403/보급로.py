import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, j):
    # v[i][j] = 0
    q = [(i,j)]
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
                q.append((ni,nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    v = [[100000]*N for _ in range(N)]
    v[0][0] = 0
    bfs(0,0)
    ans = v[-1][-1]
    print(f'#{tc} {ans}')
