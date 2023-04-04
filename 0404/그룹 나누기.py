import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
    lst = list(map(int, input().split()))
    for i in range(M):
        s, e = lst[i*2], lst[i*2+1]
        adj[s].append(e)
        adj[e].append(s)
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            q = [i]
            while q:
                t = q.pop(0)
                if adj[t]:
                    for j in adj[t]:
                        if visited[j] == 0:
                            visited[j] = 1
                            q.append(j)
    print(f'#{tc} {cnt}')
