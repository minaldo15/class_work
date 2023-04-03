import sys
sys.stdin = open('input.txt', 'r')

dy = [1,1,-1,-1]
dx = [1,-1,-1,1]
def dfs(y, x, path, way):
    global cnt, i, j

    if (y, x) == (i, j) and way == 3 and len(path) > 2:
        cnt = max(cnt, len(path))
        return
    if 0<=y<N and 0<=x<N and arr[y][x] not in path:
        # 직진
        ny, nx = y+dy[way], x+dx[way]
        dfs(ny, nx, path+[arr[y][x]], way)
        # 꺾는 경우
        if way < 3:
            ny, nx = y + dy[way+1], x + dx[way+1]
            dfs(ny, nx, path+[arr[y][x]], way+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = -1
    for i in range(N):
        for j in range(N):
            dfs(i,j,[],0)

    print(f'#{tc} {cnt}')