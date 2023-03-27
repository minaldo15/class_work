import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j):
    global v, cnt, MIN
    if MIN < cnt:   # 최솟값이 이미 cnt보다 작으면 가지치기
        return
    if (i, j) == (N - 1, N - 1):
        MIN = cnt
        return
    for di, dj in (1,0),(0,1):
        ni, nj = i+di, j+dj
        if not (0 <= ni < N and 0 <= nj < N) or v[ni][nj]:
            continue
        else:
            v[ni][nj] = 1
            cnt += arr[ni][nj]
            dfs(ni,nj)
            cnt -= arr[ni][nj]  # 원상복구
            v[ni][nj] = 0   # 미방문 처리


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    # 임의의 최솟값 설정(오른쪽으로 쭉 아래로쭉 가는 경로)
    MIN = 0
    MIN += sum(arr[0])
    for k in range(1, N):
        MIN += arr[k][-1]
    cnt = arr[0][0]
    dfs(0,0)
    print(f'#{tc} {MIN}')
