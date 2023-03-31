import sys
sys.stdin = open('input.txt','r')

def dfs(i):
    global p, ans
    if p < ans:
        return
    if i == N:
        ans = max(ans, p)
        return
    for j in range(i, N):
        lst[i], lst[j] = lst[j], lst[i]
        p = p*arr[i][lst[i]]
        dfs(i+1)
        p = p / arr[i][lst[i]]
        lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = 0.1
    lst = [x for x in range(N)]
    ans = 0
    p = 1
    dfs(0)
    ans = round(ans/100**(N-1),6)
    ans = format(ans,".6f")
    print(f'#{tc} {ans}')
