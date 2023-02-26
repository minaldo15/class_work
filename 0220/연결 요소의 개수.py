import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [0]*(N+1)
visit = [0]*(N+1)
cnt = 0
for m in range(M):
    u, v = map(int, input().split())
    if graph[u]:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if graph[v]:
        graph[v].append(u)
    else:
        graph[v] = [u]
print(graph)
for i in range(1, N+1):
    if visit[i] == 0:
        print(visit)
        visit[i] = 1
        cnt += 1
        while True:
            if graph[i]:
                for num in graph[i]:
                    if visit[num] != 1:
                        i = num
                        visit[i] = 1
                else:
                    break
            else:
                break

print(visit)
print(cnt)



