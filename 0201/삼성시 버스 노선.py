# 정류장 : P
# 노선 : N
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    check = []
    C_lst = []
    for i in range(1, N + 1):
        A, B = map(int, input().split())
        for k in range(A, B + 1):
            check.append(k)
    P = int(input())
    for j in range(1, P + 1):
        cnt = 0
        C = int(input())
        for k in check:
            if k == C:
                cnt += 1
        C_lst.append(cnt)

    print(f'#{t}', *C_lst)
