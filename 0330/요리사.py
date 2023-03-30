import sys
sys.stdin = open('input.txt', 'r')

def dfs(i,k):
    global A, B, MIN
    if i == k:
        print(A)
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [x for x in range(N)]
    A = B = 0
    MIN = 20000
    dfs(0,N)
    print(f'#{tc} {MIN}')
