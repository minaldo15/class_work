import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    print(f'#{t} {(max(ai)) - (min(ai))}')
