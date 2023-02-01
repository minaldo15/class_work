T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    # sort 안쓰고 풀어보자
    for i in range(N - 1):
        for n in range(N - 1 - i):
            if lst[n] > lst[n+1]:
                lst[n], lst[n+1] = lst[n+1], lst[n]
    print(f'#{t} {" ".join(map(str, lst))}')