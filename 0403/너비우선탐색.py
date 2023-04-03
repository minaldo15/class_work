import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, k):
    v[i] = 1
    q = [i]
    while q:
        w = q.pop(0)
        for j in adjL[w]:
            if v[j] == 0:
                alst.append(j)
                q.append(j)
                v[j]= 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    v = [0]*(V+1)
    alst = [1]
    for _ in range(E):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)
    for graph in adjL:
        graph.sort()
    bfs(1, V)
    print(f'#{tc}', *alst)