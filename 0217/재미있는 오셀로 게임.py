import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1
    dr = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for m in range(M):
        b, a, bw = map(int, input().split())
        arr[a - 1][b - 1] = bw
        for i in range(8):
            cy, cx = a - 1, b - 1
            if 0 <= cy + dr[i][0] < N and 0 <= cx + dr[i][1] < N: # 배열 범위 안에서
                if arr[cy+dr[i][0]][cx+dr[i][1]] != 0 and arr[cy+dr[i][0]][cx+dr[i][1]] != bw: # 0이 아니고 색깔 다른 돌이면
                    ny, nx = cy+dr[i][0], cx+dr[i][1] # 탐색해볼만 한 돌
                    # 배열 안에서 0이 아닌 숫자에 한해서
                    while 0 <= ny + dr[i][0] < N and 0 <= nx + dr[i][1] < N and arr[ny+dr[i][0]][nx+dr[i][1]] != 0:
                        if arr[ny + dr[i][0]][nx + dr[i][1]] == bw: # 그 방향으로 계속 탐색해서 bw이랑 같은 색이 나오면
                            cy += dr[i][0]
                            cx += dr[i][1]
                            arr[cy][cx] = bw
                            if (cy, cx) == (ny, nx): # 그 사이에 있는 돌 다 바꿀때까지 bw로 바꿈
                                break
                        else:
                            ny += dr[i][0]
                            nx += dr[i][1]
    B = 0
    A = N*N - B
    for lst in arr:
        for bw in lst:
            if bw == 1:
                B += 1
    print(f'#{t} {B} {A}')







                    




    # print(arr)