T = int(input())
for t in range (1, T + 1):
    N = int(input())
    lst = [2, 3, 5, 7, 11]
    cnt_lst = []
    for k in lst:
        cnt = 0
        if N % k == 0:
            while True:
                N = N // k
                cnt += 1
                if N % k != 0:
                    break
        cnt_lst.append(cnt)

    print(f'#{t} {" ".join(map(str, cnt_lst))}')