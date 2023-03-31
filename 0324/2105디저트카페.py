import sys
sys.stdin = open('input.txt','r')

dr = [(1,1),(1,-1),(-1,-1),(-1,1)]
def bfs(i,j):
    v = [[0]*N for _ in range(N)]
    q = [(i,j)]
    k = 0
    alst = [arr[i][j]]
    while q and k <= 3:
        ci, cj = q.pop(0)
        ni, nj = ci+dr[k][0], cj+dr[k][1]
        if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
            if arr[ni][nj] not in alst:
                q.append((ni,nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])
            else:
                if (ni, nj) == (i, j):
                    print(alst)
                    return
                k += 1
                q.append((ci, cj))
        else:
            k += 1
            q.append((ci,cj))

    # print(alst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs(0,1)
    bfs(0,2)
    bfs(0,0)