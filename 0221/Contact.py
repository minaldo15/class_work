import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    visited = [0]*101
    q = [s]
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    max = 0
    for j in range(101):
        if visited[j] >= max:
            max = visited[j]
            max_j = j
    return max_j

for t in range(1, 11):
    N, s = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(N//2):
        a, b = lst[i*2], lst[i*2+1]
        graph[a].append(b)
    ans = bfs(s)
    print(f'#{t} {ans}')
