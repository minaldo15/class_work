import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, k):  # 중복없이 빠짐없이
    v[i] = 1    # 중복방지용
    alst.append(i)
    for j in adjL[i]:   # i와 인접하고
        if v[j] == 0:   # 방문한적이 없는 j가 있으면
            dfs(j, k)
    # for j in range(1, k+1):
    #     if adjM[i][j] == 1 and v[j]==0:
    #         dfs(j, k)

def dfs2(s, k):
    stk = []
    v = [0] * (k + 1)
    i = s
    while True:
        if v[i] ==0:
            alst.append(i)
            v[i] = 1
        for j in range(1, k+1):
            if adjM[i][j] and v[j]==0:
                stk.append(i)
                i = j
                break
        else:
            if stk:
                i = stk.pop()
            else:
                break

def dfs3(i, k, g):
    global cnt
    if i == g:
        cnt += 1
    else:
        v[i] = 1    # 중복방지용
        for j in range(1, k+1):
            if adjM[i][j]==1 and v[j]==0:
                dfs3(j, k, g)
        v[i] = 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in range(V+1)]
    adjL = [[] for _ in range(V+1)]
    v = [0]*(V+1)
    alst = []
    cnt = 0
    for _ in range(E):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
        adjL[a].append(b)
        adjL[b].append(a)
    # dfs(1, V)
    dfs2(1, V)
    dfs3(1, V, 7)
    print(f'#{tc}', *alst)
    print(cnt)