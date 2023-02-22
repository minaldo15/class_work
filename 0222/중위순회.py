import sys
sys.stdin = open('input.txt', 'r')

def ino(s):
    if s:  # 존재하는 노드라면 처리
        ino(L[s])
        print(s, end=' ')
        ino(R[s])

for t in range(1, 2):
    N = int(input())
    words = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    for _ in range(N):
        lst = (list(input().split()))
        if len(lst) == 4:
            i, a, l, r = lst
            words[int(i)] = a
            L[int(i)] = int(l)
            R[int(i)] = int(r)
        elif len(lst) == 3:
            i, a, l = lst
            words[int(i)] = a
            L[int(i)] = int(l)
        else:
            i, a = lst
            words[int(i)] = a
    print(f'#{t}', end = ' ')
    ino(1)
    print()
    print(L)
    print(R)





