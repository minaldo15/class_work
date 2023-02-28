import sys
sys.stdin = open('input.txt', 'r')

def f(i, j, n):
    if n == 1:
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
    elif n == 2:
        dir = [(1,0),(-1,0)]
    elif n == 3:
        dir = [(0,1),(0,-1)]
    elif n == 4:
        dir = [(-1,0),(0,1)]
    elif n == 5:
        dir = [(1,0),(0,1)]
    elif n == 6:
        dir = [(1,0),(0,-1)]
    elif n == 7:
        dir = [(-1,0),(0,-1)]
    return dir

def bfs(i, j, k):
    global cnt
    check = {(1, 0): [1, 2, 4, 7], (-1, 0): [1, 2, 5, 6], (0, 1): [1, 3, 6, 7], (0, -1): [1, 3, 4, 5]}
    q = [(i, j)]
    v[i][j] = 1
    cnt += 1
    while q:
        ci, cj = q.pop(0)
        for (di, dj) in f(ci, cj, arr[ci][cj]):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] in check[(di, dj)]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if v[ni][nj] <= k:
                    cnt += 1
                else:
                    break
    return cnt

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [([0]*M) for _ in range(N)]
    cnt = 0
    ans = bfs(R, C, L)
    print(f'#{t} {ans}')