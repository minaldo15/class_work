import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    alst = [0]*(N+1)
    for _ in range(M):
        idx, num = map(int, input().split())
        alst[idx] = num

    for i in range(N - M, 0, -1):
        if i*2+1 <= N:
            alst[i] = alst[i*2] + alst[i*2+1]
        else:
            alst[i] = alst[i*2]
    ans = alst[L]
    print(f'#{t} {ans}')
