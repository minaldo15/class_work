from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_1 = 0
    max_2 = 0
    for i in range(N):
        for j in range(N-M+1):
            lst = arr[i][j:j+M]
            result = []
            first = 0
            for k in range(1, M+1):
                result += list(combinations(lst, k))
            for case in result:
                cnt = 0
                if sum(case) <= C:
                    for num in case:
                        cnt += num**2
                if cnt > first:
                    first = cnt

            if first > max_1:
                max_1 = first
                max_i, max_j = i, j


    for y in range(N):
        for x in range(N - M + 1):
            result1 = []
            sec = 0
            if y == max_i:
                if x+M <= max_j or x >= max_j+M:
                    lst1 = arr[y][x:x + M]
                    for l in range(1, M + 1):
                        result1 += list(combinations(lst1, l))
                    for case1 in result1:
                        cnt1 = 0
                        if sum(case1) <= C:
                            for num1 in case1:
                                cnt1 += num1 ** 2
                        if cnt1 > sec:
                            sec = cnt1
            else:
                lst1 = arr[y][x:x + M]
                for l in range(1, M + 1):
                    result1 += list(combinations(lst1, l))
                for case1 in result1:
                    cnt1 = 0
                    if sum(case1) <= C:
                        for num1 in case1:
                            cnt1 += num1 ** 2
                    if cnt1 > sec:
                        sec = cnt1
            if sec > max_2:
                max_2 = sec


    print(f'#{tc} {max_1 + max_2}')
