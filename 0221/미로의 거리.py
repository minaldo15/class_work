import sys
sys.stdin = open('input.txt', 'r')

def bfs(i,j, N):
    q = [(i,j)]
    visited[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1:
                if visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[ci][cj] + 1

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    bfs(si,sj,N)
    if visited[ei][ej] != 0:
        ans = visited[ei][ej] - 2
    else:
        ans = 0
    print(f'#{t} {ans}')
