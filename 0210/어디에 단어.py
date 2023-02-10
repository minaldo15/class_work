import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == K:
                ans += 1
            else:
                if cnt == K + 1:
                    ans -= 1
    arr1 = list(zip(*arr))
    for lst in arr1:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == K:
                ans += 1
            else:
                if cnt == K + 1:
                    ans -= 1

    print(f'#{t} {ans}')














