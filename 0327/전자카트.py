import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, k):
    global MIN
    Alst = A[:]
    cnt = 0
    if i==k:
        Alst.append(1)
        Alst.insert(0,1)
        for l in range(len(Alst)-1):
            cnt += arr[Alst[l]-1][Alst[l+1]-1]
        MIN = min(MIN, cnt)

    for j in range(i, k):
        A[i],A[j] = A[j],A[i]
        dfs(i+1, k)
        A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [x for x in range(2, N + 1)]
    MIN = 0
    for i in range(N-1):
        MIN += arr[i][i+1]
    MIN += arr[N-1][0]
    dfs(0, N-1)
    print(f'#{tc} {MIN}')
