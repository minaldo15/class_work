import sys
sys.stdin = open('input.txt')

def dfs(i,sm):
    global ans
    if ans >= sm:
        return
    if i == N:
        ans = max(ans, sm)
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(i+1, sm*(arr[i][j]/100))
            v[j] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    ans = 0
    dfs(0, 1)
    print(f'#{tc} {ans*100:.6f}')