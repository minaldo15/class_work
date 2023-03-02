import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    # ans = N ** 2
    for i in range(N):
        for j in range(N):
            cnt = 0
            ci, cj = i, j
            while True:
                x = arr[ci][cj]
                for di, dj in (1,0),(-1,0),(0,1),(0,-1):
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == x + 1:
                            cnt += 1
                            ci, cj = ni, nj
                            break
                else:
                    break
            if cnt > max:
                max = cnt
                ans = x - cnt
            if max > 0:
                if cnt == max:
                    if ans > x - cnt:
                        ans = x - cnt

    print(f'#{t} {ans} {max + 1}')
