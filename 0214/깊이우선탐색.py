import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split()) # V: 정점 개수 E: 연결선 개수
    adjl = [[] for _ in range(V + 1)] # 인접행렬
    for e in range(E):
        v1, v2 = map(int, input().split())
        adjl[v1].append(v2)
        adjl[v2].append(v1)

    stk = [1]
    visit = [1]
    j = 0
    while True:
        if stk:
            if adjl[stk[-1]][j] not in visit:
                visit.append(adjl[stk[-1]][j])
                stk.append(adjl[stk[-1]][j])
                j = 0
            else:
                if j == len(adjl[stk[-1]]) - 1:
                    j = 0
                    stk.pop()
                else:
                    j += 1
        else:
            break

    print(f'#{t}', *visit)



