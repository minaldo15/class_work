import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for lst in arr:
        cnt = 0
        for num in lst:
            if num == 1:
                cnt += 1
                if num == lst[-1]:
                    if cnt > max:
                        max = cnt
            else:
                if cnt > max:
                    max = cnt
                cnt = 0
    arr1 = list(zip(*arr))
    print(arr1)
    for lst in arr1:
        cnt = 0
        for num in lst:
            if num == 1:
                cnt += 1
                if num == lst[-1]:
                    if cnt > max:
                        max = cnt
            else:
                if cnt > max:
                    max = cnt
                cnt = 0
    print(f'#{t} {max}')
