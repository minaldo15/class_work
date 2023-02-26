import sys
sys.stdin = open('input.txt', 'r')

def f(i, j, n):
    nlst = []
    if n == 1:
        for di,dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = i + di, j + dj
            if (di, dj) == (1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (-1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 5 or arr[ni][nj] == 6:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, 1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 6 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, -1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 5:
                    nlst.append((ni, nj))
        return nlst
    elif n == 2:
        for di,dj in (1,0),(-1,0):
            ni, nj = i + di, j + dj
            if (di, dj) == (1,0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (-1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 5 or arr[ni][nj] == 6:
                    nlst.append((ni, nj))
        return nlst
    elif n == 3:
        for di,dj in (0,1),(0,-1):
            ni,nj = i+di, j+dj
            if (di, dj) == (0, 1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 6 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, -1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 5:
                    nlst.append((ni, nj))
        return nlst
    elif n == 4:
        for di,dj in (-1,0),(0,1):
            ni,nj = i+di, j+dj
            if (di, dj) == (-1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 5 or arr[ni][nj] == 6:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, 1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 6 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
        return nlst
    elif n == 5:
        for di,dj in (1,0),(0,1):
            ni,nj = i+di, j+dj
            if (di, dj) == (1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, 1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 6 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
        return nlst
    elif n == 6:
        for di,dj in (1,0),(0,-1):
            ni,nj = i+di, j+dj
            if (di, dj) == (1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 7:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, -1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 5:
                    nlst.append((ni, nj))
        return nlst
    elif n == 7:
        for di,dj in (-1,0),(0,-1):
            ni,nj = i+di, j+dj
            if (di, dj) == (-1, 0):
                if arr[ni][nj] == 1 or arr[ni][nj] == 2 or arr[ni][nj] == 5 or arr[ni][nj] == 6:
                    nlst.append((ni, nj))
            elif (di, dj) == (0, -1):
                if arr[ni][nj] == 1 or arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 5:
                    nlst.append((ni, nj))
    return nlst

def bfs(i, j, k):
    cnt = 0
    q = [(i, j)]
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for (ni, nj) in f(ci, cj, arr[ci][cj]):
            if 0<=ni<N and 0<=nj<M:
                if v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
    for y in range(N):
        for x in range(M):
            if 0 < v[y][x] <= k:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [([0]*M) for _ in range(N)]
    ans = bfs(R, C, L)
    print(f'#{t} {ans}')