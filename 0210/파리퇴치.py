import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N-M+1):
        for j in range(N - M + 1):
            sum = 0
            for y in range(M):
                for x in range(M):
                    sum += arr[i+y][j+x]
            if sum > max:
                max = sum
    print(f'#{t} {max}')
