import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    idx = M % N
    print(f'#{t} {nums[idx]}')
