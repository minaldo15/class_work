import copy
import sys
sys.stdin = open('input.txt', 'r')

def bfs(i,j):
    v = [[0]*N for _ in range(N)]
    q = [(i, j)]
    v[i][j] = 1
    max = 0
    while q:
        ci, cj = q.pop(0)
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]<arr[ci][cj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
                if v[ni][nj] > max:
                    max = v[ni][nj]
    return max


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    ans1 = 0
    for i in range(N):
        for j in range(N):
            arr1 = copy.deepcopy(arr)
            arr1[i][j] = arr[i][j] - K
            max = 0
            for y in range(N):
                for x in range(N):
                    if arr1[y][x] > max:
                        max = arr1[y][x]
            for y in range(N):
                for x in range(N):
                    if arr1[y][x] == max:
                        cnt = bfs(y, x)
                        if cnt > ans:
                            ans = cnt
    top = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > top:
                top = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                cnt = bfs(i, j)
                if cnt > ans1:
                    ans1 = cnt
    if ans>ans1:
        fans = ans
    else:
        fans = ans1
    print(f'#{tc} {fans}')
