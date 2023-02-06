T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = 10
    flag = 0 # 부분집합의 합이 0이 되는 것이 존재하는 지 판별
    for i in range(1<<n): # 부분집합의 개수
        sum = 0
        for j in range(n): # 원소의 수만큼 비트를 비교함
            if i & (1<<j):
                sum += arr[j]
                print(arr[j])
        print(sum)
        if sum == 0:
            flag += 1
            break
    print(f'#{t} {flag}')
