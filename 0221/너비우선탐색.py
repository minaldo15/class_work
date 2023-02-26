import sys
sys.stdin = open('input.txt', 'r')

def bfs(v, N):
    visited = [0]*(N+1) # 방문표시(인큐 표시)
    q = [v] # 큐에 만들고 시작점 넣기
    visited[v] = 1 # 시작점 인큐
    while q:
        t = q.pop(0) # 방문, 디큐
        ans.append(t) # 리스트(ans)에 경로 표시
        for i in graph[t]: # t에 인접한 i탐색
            if visited[i] == 0: # v가 0이면 즉, 큐에 없으면
                q.append(i)
                visited[i] = visited[t] + 1
    # print(visited)

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    ans = []
    for e in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    bfs(1, V)

    print(f'#{t}', *ans)
