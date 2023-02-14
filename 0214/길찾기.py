import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    T, E = map(int, input().split())
    arr = list(map(int, input().split()))
    node = [[] for _ in range(100)]  # 인접리스트
    for i in range(E):
        s, e = arr[i * 2], arr[i * 2 + 1]
        node[s].append(e)
    stk = [0]
    visited = [False for _ in range(100)]
    while stk:
        now = stk.pop()
        visited[now] = True
        for next in node[now]:
            if visited[next] == False:
                stk.append(next)

    if visited[e] == True:
        answer = 1
    else:
        answer = 0
    print(f'#{T} {answer}')