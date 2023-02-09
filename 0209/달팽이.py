N = int(input())
C = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [([0] * N) for _ in range(N)]
x = y = N//2
dir = -1
arr[y][x] = 1
for k in range(2, N*N + 1):
    # if 0<= y+dy[dir+1] < N and 0 <= x+dx[dir+1] < N:
        if arr[y+dy[dir+1]][x+dx[dir+1]] == 0:
            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
            arr[y][x] = k
        else:
            x += dx[dir]
            y += dy[dir]
            arr[y][x] = k
print(arr)



