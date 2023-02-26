import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, v):
    global ans
    global fcnt
    fcnt += 1
    # 가지치기는 제일 위(최소값)
    if ans <= sm:
        return

    elif n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        # 세번째 (오래걸림)
        if j not in v:
            dfs(n + 1, sm + arr[n][j], v+[j])
        # 두번째
        # if j not in v:
        #     v.append(j)
        #     dfs(n+1, sm+arr[n][j])
        #     v.pop()
        # 첫번째
        # if v[j] == 0:
        #     v[j] = 1
        #     dfs(n+1, sm+arr[n][j])
        #     v[j] = 0  # 사용 후 반드시 clear

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10*N
    v = []  # 첫번째 [0]*N
    fcnt = 0
    dfs(0, 0, v)

    print(f'#{t} {ans}')
    # print(fcnt)




