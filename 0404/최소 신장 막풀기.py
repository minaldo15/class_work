import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    cnt = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    for branch in adj:
        branch.sort(key=lambda x:x[1])  # 가중치가 적은 간선부터 계산하기 위해
    for i in range(V+1):
        if visited[i] < 2:              # 방문횟수가 2회 이상이면 불필요한 간선이 추가된 것   
            visited[i] += 1             # 시작점(u) 방문횟수 추가
            visited[adj[i][0][0]] += 1  # 도착점(v) 또한 방문횟수 추가
            cnt += adj[i][0][1]         # 연결간선(u-v)의 가중치 더함
    for i in range(V+1):
        if visited[i]
    print(f'#{tc} {cnt}')
