import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, k):
    global MIN, cnt
    if cnt > MIN:
        return
    if i==k:
        MIN = min(MIN, cnt + arr[A[i-1]][0])

    for j in range(i, k):
        A[i],A[j] = A[j],A[i]
        cnt += arr[A[i-1]][A[i]]
        dfs(i+1, k)
        cnt -= arr[A[i - 1]][A[i]]
        A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [0] + [x for x in range(1, N)] + [0]
    cnt = 0
    MIN = 10000
    dfs(1, N)
    print(f'#{tc} {MIN}')
