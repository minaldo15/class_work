T = int(input())
for t in range(1, T + 1):
    N = T = int(input())
    a = list(map(int, input().split()))
    for i in range(N - 1):
        if i % 2 == 0:
            max_i = i
            for j in range(i + 1, N):
                if a[max_i] < a[j]:
                    max_i = j
            a[i], a[max_i] = a[max_i], a[i]
        else:
            min_i = i
            for j in range(i + 1, N):
                if a[min_i] > a[j]:
                    min_i = j
            a[i], a[min_i] = a[min_i], a[i]
    ans = a[:10]
    print(f'#{t}', *ans)

