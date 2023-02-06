T = int(input())
for t in range (1, T + 1):
    N = int(input())
    lst = [2, 3, 5, 7, 11]
    cnt_lst = []
    for k in lst:
        cnt = 0
        while N % k == 0:
            N = N // k
            cnt += 1
        cnt_lst.append(cnt)

    print(f'#{t}', *cnt_lst)