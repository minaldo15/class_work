
T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
for t in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        sub_set = []
        sum = 0
        for j in range(12): # 원소의 수만큼 비트를 비교함
            if i & (1<<j):
                sub_set.append(A[j])
                sum += A[j]
        if len(sub_set) == N and sum == K:
            result += 1
    print(f'#{t} {result}')

