import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, chance):
    global MAX, visited
    MAX = max(MAX, visited[i][j])
    for di, dj in (1,0),(-1,0),(0,1),(0,-1):
        ni, nj = i+di, j+dj
        if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj]:
            continue
        if A[i][j] > A[ni][nj]: # next의 높이가 더 낮으면(깎을 필요 x)
            visited[ni][nj] = visited[i][j] + 1
            dfs(ni, nj, chance)
            visited[ni][nj] = 0 # 미방문 처리
        elif chance and A[ni][nj] - K < A[i][j]:    # 깎을 기회가 남아있고, 깎아서 낮게 만들 수 있으면(최대 K만큼 깎았을 때 현재위치보다 낮다면)
            temp = A[ni][nj]    # 깎기 전의 next 높이 기억
            A[ni][nj] = A[i][j] - 1 # next 높이가 현재 높이보다 1만 낮게 깎음(그래야 더 갈 수있는 경로가 늘어남, 조금만 깎아야)
            visited[ni][nj] = visited[i][j] + 1
            dfs(ni, nj, chance-1)   # 깎을 기회 쓴 상태로 다시 dfs
            visited[ni][nj] = 0 # 미방문 처리
            A[ni][nj] = temp    # 깎은 위치 높이도 다시 원상태로

# main
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = []
    top = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j] > top:
                top = A[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print(f'#{tc} {MAX}')
