import sys
sys.stdin = open('input.txt', 'r')


def f(i, N, K):
    global cnt
    if i == N:
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += A[j]
        if s == K:
            cnt += 1

    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i + 1, N, K)



T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    bit = [0] * N
    cnt = 0
    f(0, N, K)
    print(f'#{t} {cnt}')
