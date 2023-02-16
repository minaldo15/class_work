import sys
sys.stdin = open('input.txt', 'r')

def f(i, N, K):
    global ans
    if i == 12:
        s = 0 # 원소의 합
        cnt = 0 # 원소의 개수
        for j in range(12):
            if bit[j] == 1:
                cnt += 1
                s += A[j]
        if cnt == N and s == K:
            ans += 1

    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i + 1, N, K)

A = [x for x in range(1, 13)]
T = int(input())
for t in range(1, T + 1):
    N, K =map(int, input().split())
    bit = [0] * 12
    ans = 0
    f(0, N, K)
    print(f'#{t} {ans}')
