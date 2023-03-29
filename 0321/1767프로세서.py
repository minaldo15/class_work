import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, j):
    q = [(i,j)]
    v[i][j] = 1
    for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
        while q:
            ci, cj = q.pop(0)
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))
            else:
                q = [(i, j)]
                break
        if ni == -1 or ni == N or nj == -1 or nj == N:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    ans = 0
    alst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and 0<i<N-1 and 0<j<N-1:
                bfs(i, j)
    print(v)



