import sys
sys.stdin = open('input.txt','r')

def dfs(i, sm):
    if sm > K:
        return
    global ans
    if i == N:
        if sm == K:
            ans += 1
        return
    dfs(i+1, sm+A[i])   # 포함
    dfs(i+1, sm)        # 미포함

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f'#{tc} {ans}')
