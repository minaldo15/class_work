import sys
sys.stdin = open('input.txt', 'r')

def bfs(i,j, N):
    q = [(i,j)]
    visited[i][j] = 1
    while q:
        t = q.pop() # t == (i,j)
        # visit(t)
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni, nj = t[0]+di, t[1]+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                if visited[ni][nj] == 0: # v가 0이면 즉, 큐에 없으면
                    q.append((ni,nj))
                    visited[ni][nj] = visited[t[0]][t[1]] + 1

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                si,sj = y,x
            elif arr[y][x] == 3:
                ei, ej = y, x
    bfs(si,sj, N)
    if visited[ei][ej] != 0:
        ans = 1
    else:
        ans = 0
    print(f'#{t} {ans}')
