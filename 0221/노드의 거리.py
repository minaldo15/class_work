import sys
sys.stdin = open('input.txt', 'r')

def bfs(s, g, N):
    visited = [0]*(N+1)
    q = [s]
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    if visited[g] != 0:
        return visited[g] - 1
    else:
        return 0

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    # print(graph)
    ans = bfs(S, G, V)
    print(f'#{t} {ans}')
