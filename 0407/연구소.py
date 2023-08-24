import sys
sys.stdin = open('input.txt', 'r')

import itertools

def bfs(i,j):
    v1[i][j] = 1
    q = [(i,j)]
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v1[ni][nj] == 0 and arr[ni][nj] == 0:
                arr[ni][nj] = 2
                v1[ni][nj] = 1
                q.append((ni,nj))

# def dfs(n, casenum):
#     global ans
#     if n == 3:
#         cnt = 0
#         for (y, x) in virus:
#             bfs(y, x)
#         for u in range(N):
#             for v in range(M):
#                 if arr[u][v] == 0:
#                     cnt += 1
#         ans = max(ans, cnt)
#         return








N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v2 = [[0]*M for _ in range(N)]
v1 = [[0]*M for _ in range(N)]
print(arr)
virus = []
wall = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i,j))
        if arr[i][j] == 1:
            wall += 1
        if arr[i][j] == 2:
            virus.append((i,j))
        if arr[i][j] == 0:
            emty.append((i,j))
nCr = itertools.combinations(emty, 3)
allcase = list(nCr)
print(virus)
print(emty)
print(allcase)
# dfs(0)

