m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = list(zip(*arr))

col_cnt = {}
for i in range(n):
    count = [0] * 7
    for num in arr[i]:
        count[num] += 1

    max_count = count[0]
    for c in range(1, 7):
        if count[c] >= max_count:
            max_count = count[c]
            max_c = c
    col_cnt[i] = max_c, max_count
# print(col_cnt)
# col_items = col_cnt.items()
# print(col_items)
sort_col = sorted(col_cnt.items(), key=lambda x: (x[1][0], -x[0]), reverse=True)
# print(sort_col)
for idx in range(len(sort_col)):
    print(sort_col[idx][0], sort_col[idx][1][0], sort_col[idx][1][1])








