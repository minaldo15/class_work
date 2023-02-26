import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[9]*(M+2)] + [([9] + list(map(int, input().split())) + [9]) for _ in range(N)] + [[9]*(M+2)]
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            cnt = 0
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                if arr[i+di][j+dj] < arr[i][j]:
                    cnt += 1
            if cnt >= 4:
                ans += 1
    print(f'#{t} {ans}')
