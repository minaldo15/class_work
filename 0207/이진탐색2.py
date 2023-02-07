def bin_cnt(P, K):
    l = 1
    r = P
    cnt = 0
    # a = [x for x in range(1, P + 1)]
    while l <= r:
        c = int((l + r)/2)
        cnt += 1
        if c == K:
            return cnt
        elif c > K:
            r = c
        else:
            l = c
T = int(input())
for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    if bin_cnt(P, A) > bin_cnt(P, B):
        ans = 'B'
    elif bin_cnt(P, A) < bin_cnt(P, B):
        ans = 'A'
    else:
        ans = 0
    print(f'#{t} {ans}')



