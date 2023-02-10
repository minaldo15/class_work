import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    T = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    n = 2 # 회문의 길이 2부터 시작
    for lst in arr:
        for i in range(N - n + 1):
            for k in range(n, N - i + 1):
                for l in range(k//2):
                    if lst[i+l] != lst[i+k-l-1]:  # 이거 다시 짜자
                        break
                    else:
                        if l == k//2 - 1:
                            n = k
    arr1 = list(zip(*arr))
    for lst in arr1:
        for i in range(N - n + 1):
            for k in range(n, N - i + 1):
                for l in range(k // 2):
                    if lst[i + l] != lst[i + k - l - 1]:  # 이거 다시 짜자
                        break
                    else:
                        if l == k // 2 - 1:
                            n = k
    print(f'#{T} {n}')






        # for i in range(N):
        #     for k in range(2, N - i + 1):
        #         if lst[i:i+k] == lst[i:i+k][::-1]:
        #             if len(lst[i:i+k]) > max:
        #                 max = len(lst[i:i+k])


    # arr1 = list(zip(*arr))

