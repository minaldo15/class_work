import sys
sys.stdin = open('input.txt', 'r')

def f(i, j):
    v = [([0] * N) for _ in range(N)]
    q = [(i,j)]
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
    max = 0
    for k in range(1, N*2):
        cnt = 0
        for i in range(N):
            for j in range(N):
                if v[i][j] <= k:
                    if arr[i][j] == 1:
                        cnt += 1

        if cnt * M >= k*k + (k-1)*(k-1) and cnt > max:
            max = cnt
    return max


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if ans < f(i, j):
                ans = f(i, j)
    print(f'#{t} {ans}')
