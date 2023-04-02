import sys
sys.stdin = open('input.txt')

def dfs(i, sm):
    global ans
    if sm >= ans:
        return
    if i == N:
        ans = min(ans, sm+arr[A[-2]][0])
    for j in range(i, N):
        A[i],A[j] = A[j],A[i]
        sm += arr[A[i-1]][A[i]]
        dfs(i+1, sm)
        sm -= arr[A[i-1]][A[i]]
        A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [0] + [x for x in range(1,N)] + [0]
    ans = 10000
    dfs(1, 0)
    print(f'#{tc} {ans}')