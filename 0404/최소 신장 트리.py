import sys
sys.stdin = open('input.txt','r')

def find_set(x):    # x가 속한 집합의 대표 리턴
    while x != rep[x]:  # x==rep[x]까지
        x = rep[x]
    return x

def union(x,y): # y의 대표원소가 x의 대표원소
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]
    graph = []
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        graph.append([v1, v2, w])
    # 가중치 기준 오름차순 정렬
    graph.sort(key=lambda x:x[2])
    # N개 정점(v+1), N-1개의 간선 선택
    N = V + 1
    s = 0           # MST에 포함된 간선의 가중치 합
    cnt = 0
    MST = []
    for v, u, w in graph:   # 가중치가 작은 것부터...
        if find_set(u) != find_set(v):
            cnt += 1
            s += w
            MST.append([v,u,w])
            union(u, v)
            if cnt==N-1:
                break
    print(f'#{tc} {s}')
