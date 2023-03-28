import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, k):
    global cnt, MIN
    if cnt > MIN:
        return
    if i == k:
        MIN = cnt
    for j in range(i, k):
        A[i], A[j] = A[j], A[i]
        cnt += arr[i][A[i]]
        dfs(i + 1, k)
        cnt -= arr[i][A[i]]
        A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [x for x in range(N)]
    MIN = 0
    cnt = 0
    for i in range(N):
        MIN += arr[i][i]
    dfs(0, N)
    print(f'#{tc} {MIN}')
