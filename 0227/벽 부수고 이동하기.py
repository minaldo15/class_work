import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, j):
    min = m*n
    while True:
        v = [[0] * m for _ in range(n)]
        q = [(0, 0)]
        v[0][0] = 1
        flag = 0
        while q:
            ci, cj = q.pop(0)
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0:
                    if arr[ni][nj] == 1:
                        if flag == 0:
                            if arr[ni+di][nj+dj] == 0 and wall[ni][nj] == 0:    # 010일때
                                q.append((ni, nj))
                                v[ni][nj] = v[ci][cj] + 1
                                wall[ni][nj] = 1
                                flag = 1
                    else:
                        q.append((ni, nj))
                        v[ni][nj] = v[ci][cj] + 1

            if v[ni][nj] >= min:
                break
        if v[n-1][m-1] == 0:
            break
        else:
            if v[n-1][m-1] < min:
                min = v[n-1][m-1]
    return min

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
wall = [[0] * m for _ in range(n)]
ans = bfs(0,0)
print(ans)
