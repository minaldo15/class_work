T = int(input())
for t in range(1, T + 1):
    N, Q = map(int , input().split())
    lst = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int , input().split())
        for j in range(L, R + 1):
            lst[j - 1] = i
    print(f'#{t}', *lst)