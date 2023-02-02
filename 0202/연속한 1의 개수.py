T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = 1
    max = 0
    for i in range(N - 1):
        if lst[i] == 1:
            if lst[i + 1] == 1:
                cnt += 1
            else: # lst[i + 1] == 0
                cnt = 1
        if cnt > max:
            max = cnt    
    print(f'#{t} {max}')



