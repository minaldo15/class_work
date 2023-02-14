import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    for e in range(E):
        v1, v2 = map(int, input().split())
        node[v1].append(v2)
    S, G = map(int, input().split())
    stk =[S]
    visited = [False for _ in range(V + 1)]
    while stk:
        now = stk.pop()
        visited[now] = True
        for next in node[now]:
            if visited[next] == False:
                stk.append(next)
        print(visited)
    if visited[G] == True:
        answer = 1
    else:
        answer = 0

    print(f'#{t} {answer}')
