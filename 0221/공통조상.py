import sys
sys.stdin = open('input.txt', 'r')

def bfs(x):
    v = [0]*(V+1)
    q = [x]
    v[x] = 1
    parent = []
    while q:
        t = q.pop(0)
        parent.append(t)
        for i in graph_B[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t] + 1
    return parent

def bfs1(s):
    cnt = 0
    v = [0]*(V+1)
    q = [s]
    v[s] = 1
    cnt += 1
    while q:
        t = q.pop(0)
        for i in graph_F[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = 1
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    V, E, x, y = map(int, input().split())
    lst = list(map(int, input().split()))
    graph_B = [[] for _ in range(V+1)] # 밑에서 부터 위로 탐색하는 그래프
    graph_F = [[] for _ in range(V+1)] # 위에서 부터 밑으로 탐색하는 그래프 -> 서브트리의 크기 구하기
    for i in range(E):
        a, b = lst[i*2], lst[i*2+1]
        graph_B[b].append(a)
        graph_F[a].append(b)

    px = bfs(x)
    py = bfs(y)
    # 서브트리 s 찾기
    for p in px:
        if p in py:
            s = p
            break  # 가까이에 있는 공통조상 찾고 끝
    ans = bfs1(s)
    print(f'#{t} {s} {ans}')
