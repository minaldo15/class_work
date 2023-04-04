import sys
sys.stdin = open('input.txt','r')

def dfs(s, w):
    global ans
    if w >= ans:
        return
    if s == V-1:
        ans = min(ans, w)
    for i in adjL[s]:
        if visited[i[0]] == 0:
            visited[i[0]] = 1
            dfs(i[0], w+i[1])
            visited[i[0]] = 0
T= int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V)]
    visited = [0]*V
    ans = 100000
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjL[u].append((v,w))
    dfs(0, 0)
    print(f'#{tc} {ans}')
