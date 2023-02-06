import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    sum += abs(arr[i][j] - arr[ni][nj])
    print(f'#{t} {sum}')

