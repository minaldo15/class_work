import sys
sys.stdin = open('input.txt','r')

d = [(1,1),(1,-1),(-1,-1),(-1,1)]

def bfs(i, j):
    k = 0
    lst = [arr[i][j]]
    q = [(i, j)]
    while k < 4:
        ci, cj = q.pop(0)
        ni, nj = ci+d[k][0], cj+d[k][1]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] not in lst:
                lst.append(arr[ni][nj])
                q.append((ni, nj))
            else:
                if (ni,nj) == (i,j):
                    return len(lst)
                k += 1
                q.append((ci, cj))
        else:
            k += 1
            q.append((ci, cj))
    return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MAX = -2
    for i in range(N-2):
        for j in range(1, N-1):
            MAX = max(MAX, bfs(i, j))
    print(f'#{tc} {MAX}')
