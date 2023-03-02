import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(s):
    q = deque([s])
    while q:
        t = q.popleft()
        for i in graph[t]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
v = [0]*(N+1)
cnt = 0
for _ in range(M ):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if v[i] == 0:
        if graph[i]:
            bfs(i)
            cnt += 1
        else:
            cnt += 1
            v[i] = 1
print(cnt)












