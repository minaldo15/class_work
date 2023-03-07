N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
B = [[0]*N for _ in range(N)]   # 비숍이 있나없나

def bfs(i,j):
    flag = 0
    for di, dj in (1, 1), (-1, -1), (-1, 1), (1, -1):
        q = [(i, j)]
        while q:
            ci, cj = q.pop(0)
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N:
                q.append((ni,nj))
                if B[ni][nj] == 1:
                    flag = 1
                    break
    return flag

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            f = bfs(i, j)
            if f == 0:
                B[i][j] = 1
                cnt += 1
print(cnt)
            
