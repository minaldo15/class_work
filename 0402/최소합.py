import sys
sys.stdin = open('input.txt')

def dfs(i,j,sm):
    global MIN
    if sm >= MIN:
        return
    if (i,j) == (N-1,N-1):
        MIN = min(MIN, sm)
        return
    if i < N-1:
        dfs(i+1, j, sm+arr[i+1][j])
    if j < N-1:
        dfs(i, j+1, sm+arr[i][j+1])
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MIN = 99999
    dfs(0,0,arr[0][0])
    print(f'#{tc} {MIN}')
