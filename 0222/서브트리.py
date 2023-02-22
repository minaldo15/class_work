import sys
sys.stdin = open('input.txt', 'r')

def f(s):
    global cnt
    if s:
        cnt += 1
        f(L[s])
        f(R[s])

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    L = [0]*(E+2)
    R = [0]*(E+2)
    cnt = 0
    for i in range(E):
        a, b = lst[i*2], lst[i*2 + 1]
        if L[a]:
            R[a] = b
        else:
            L[a] = b
    f(N)
    print(f'#{t} {cnt}')
