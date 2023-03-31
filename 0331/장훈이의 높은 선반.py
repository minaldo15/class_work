import sys
sys.stdin = open('input.txt','r')

def dfs(i, sm):
    global MIN
    if sm > MIN:
        return
    if i == N:
        if sm >= B:
            MIN = min(MIN, sm)
        return
    dfs(i+1, sm+lst[i])
    dfs(i + 1, sm)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    MIN = 200000
    dfs(0, 0)
    print(f'#{tc} {MIN-B}')