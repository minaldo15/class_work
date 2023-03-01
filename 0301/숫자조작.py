import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    Q = N//P
    R = N % P
    ans = (Q+1)**R * Q**(P-R)
    print(ans)

