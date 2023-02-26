import sys
sys.stdin = open('input.txt', 'r')

def ino(s):
    if s:
        ino(L[s])
        alst.append(s)
        ino(R[s])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    alst = [0]
    for i in range(1, N//2+1):
        L[i] = i * 2
        if i * 2 + 1 <= N:
            R[i] = i * 2 + 1
    ino(1)
    root = alst.index(1)
    ans = alst.index(N//2)
    print(f'#{t} {root} {ans}')
