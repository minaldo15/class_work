T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    maximum = max(lst)
    cnt_lst = [0] * (maximum + 1)
    sort_lst = [0] * N
    for num in lst:
        cnt_lst[num] += 1
    for i in range(1, maximum + 1):
        cnt_lst[i] += cnt_lst[i - 1]
    for num in lst:
        cnt_lst[num] -= 1
        sort_lst[cnt_lst[num]] = num
    print(f'#{t} {" ".join(map(str, sort_lst))}')
