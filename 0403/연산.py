import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(s, e):
    q = deque()
    v = [0]*1000001
    q.append(s)
    v[s] = 1
    while q:
        c = q.popleft()
        if c==e:
            return v[e]-1
        for n in (c-1),(c+1),(c*2),(c-10):
            if 1<=n<=1000000 and v[n]==0:
                q.append(n)
                v[n] = v[c]+1
    return -1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{tc} {ans}')