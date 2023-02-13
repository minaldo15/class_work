import sys
sys.stdin = open('input.txt', 'r')

def power(N, M):
        if M == 1:
            return N
        else:
            return N*power(N, M-1)

for t in range(10):
    T = int(input())
    N, M = map(int, input().split())
    print(f'#{T} {power(N, M)}')
