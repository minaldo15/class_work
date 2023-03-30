def msort(lst):
    global cnt
    if len(lst) < 2:
        return lst
    m = len(lst) // 2
    left = msort(lst[:m])
    right = msort(lst[m:])

    if left[-1] > right[-1]:
        cnt += 1

    ret = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1

    ret += left[l:] + right[r:]
    return ret

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = msort(lst)
    print(f'#{tc} {lst[N // 2]} {cnt}')