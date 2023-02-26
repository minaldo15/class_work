import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    total = [x for x in range(1, N+1)]
    submit = list(map(int, input().split()))
    for sub in submit:
        total.remove(sub)
    print(f'#{t}', *total)
