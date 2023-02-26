import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, j):
    v = [([0]*16) for _ in range(16)]
    q = [(i,j)]
    v[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for di,dj in (1,0),(-1,0),(0,1),(0,-1):
            ni,nj = ci+di,cj+dj
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1:
                if v[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = 1
    return v[ei][ej]

for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    ans = bfs(si, sj)
    print(f'#{t} {ans}')
