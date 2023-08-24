import sys
sys.stdin = open('input.txt', 'r')

import itertools, copy
def bfs(i,j):
    cnt = 0
    v[i][j] = 1
    q = [(i,j)]
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr1[ni][nj] == 0:
                arr1[ni][nj] = 2
                v[ni][nj] = 1
                q.append((ni,nj))

N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
virus = []
emty = []
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        if arr[i][j] == 0:
            emty.append((i,j))
nCr = itertools.combinations(emty, 3)
allcase = list(nCr)
print(virus)
print(emty)
print(allcase)
for case in allcase:
    arr1 = copy.deepcopy(arr)
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for (i,j) in case:
        bfs(i, j)
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                cnt + 1
    if cnt > ans:
        ans = cnt
    print(ans)


