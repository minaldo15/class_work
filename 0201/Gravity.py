T = int(input())
for t in range(1, T + 1):
    N = int(input())
    t_lst = list(map(int, input().split()))
    ans = 0
    for n in range(N):
        cnt = 0
        for i in range(n + 1, N):
            if t_lst[n] <= t_lst[i]:
                continue
            else:
                cnt += 1
        ans = max(ans, cnt)
    print(f'#{t} {ans}')



