import sys
sys.stdin = open('input.txt','r')

def dfs(n, sm, i, j):
    if sm in ans:
        return
    if n == N-1:
        ans.append(sm)
        return
    for di, dj in (1,0),(-1,0),(0,1),(0,-1):
        ni,nj = i+di,j+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(n+1,sm+arr[ni][nj], ni, nj)

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    ans = []
    N = 7
    for i in range(4):
        for j in range(4):
            dfs(0, arr[i][j], i, j) # 첫번째 숫자를 넣어놓고 시작 ->(n==6 일때 리턴)
    print(f'#{tc} {len(ans)}')
