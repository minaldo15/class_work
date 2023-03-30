import sys
sys.stdin = open('input.txt', 'r')

def check(i, j):
    ci, cj = i, j
    for di, dj in (1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1):
        ni, nj = ci + di, cj + dj
        while True:
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] != 1:
                    ni += di
                    nj += dj
                else:
                    return 0
            else:
                break
    return 1

def dfs(i, k):
    global ans
    cnt = 0
    if i == k:
        for y in range(N):
            for x in range(N):
                if arr[y][x] == 1:
                    if check(y, x) == 1:
                        cnt += 1
                    else:
                        return
        if cnt == N:
            ans += 1
    for j in range(i, k):
        jlst[i], jlst[j] = jlst[j], jlst[i]
        arr[i][jlst[i]] = 1
        dfs(i+1, k)
        arr[i][jlst[i]] = 0
        jlst[i], jlst[j] = jlst[j], jlst[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= [[0]*N for _ in range(N)]
    jlst = [x for x in range(N)]
    ans = 0
    dfs(0, N)
    print(f'#{tc} {ans}')
