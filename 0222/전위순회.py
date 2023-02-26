import sys
sys.stdin = open('input.txt', 'r')

def pre(i):
    if i: # 존재하는 노드라면 처리
        print(i, end =' ')
        # alst.append(i)
        pre(L[i])
        pre(R[i])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    L = [0]*(N + 1)
    R = [0]*(N + 1)
    n = len(lst)
    for i in range(n//2):
        a, b = lst[i*2], lst[i*2 + 1]
        if L[a]:
            R[a] = b
        else:
            L[a] = b
    print(f'#{t}', end=' ')
    pre(1)
    print()