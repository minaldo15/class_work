T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    max = 0
    for i in range(N - 1):
        if lst[i] < lst[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > max:
            max = cnt
    print(f'#{t} {max}')