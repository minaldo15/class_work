import sys
sys.stdin = open('input.txt', 'r')

def bfs(i,j):
    q = [(i, j)]
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = 1

    return v[ei][ej]

for t in range(1, 11):
    T = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    v = [([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    ans = bfs(si, sj)
    print(f'#{t} {ans}')