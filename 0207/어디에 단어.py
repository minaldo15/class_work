import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
    print(arr)
    cnt = 0
    for i in range(N): # 행 검증
        c_1 = 0
        for j in range(N - 1):
            if arr[i][j] == 1:
                c_1 += 1
            else:
                c_1 = 0
            if c_1 == K:
                if arr[i][j+1] == 1:
                    c_1 = 0
                else:
                    cnt += 1
            if j == N - 2 and c_1 == K - 1:
                if arr[i][j + 1] == 1:
                    cnt += 1
    
    for j in range(N): # 열 검증
        c_1 = 0
        for i in range(N - 1):
            if arr[i][j] == 1:
                c_1 += 1
            else:
                c_1 = 0
            if c_1 == K:
                if arr[i+1][j] == 1:
                    c_1 = 0
                else:
                    cnt += 1
            if i == N - 2 and c_1 == K - 1:
                if arr[i+1][j] == 1:
                    cnt += 1
    print(cnt)






