import sys
sys.stdin = open("input.txt", "r")

for t in range(10):
    T = int(input())
    arr = []
    N = 100
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    # 행 비교
    max_row = 0
    for i in range(N): 
        sum = 0
        for j in range(N):
            sum += arr[i][j]
        # print(sum)
        if sum > max_row:
            max_row = sum
    # print(max_row)

    # 열 비교
    max_col = 0
    for j in range(N):
        sum = 0
        for i in range(N):
            sum += arr[i][j]
        # print(sum)
        if sum > max_col:
            max_col = sum
     # print(max_col)

    # 대각선 비교
    # 우하향
    sum1 = 0
    for k in range(N):
        sum1 += arr[k][k]
    # 좌하향
    sum2 = 0
    for k in range(N):
        sum2 += arr[k][N - k - 1]
    if sum1 > sum2:
        max_dig = sum1
    else:
        max_dig = sum2

    # 가로 세로 중 맥스
    if max_col > max_row:
        max_col_row = max_col
    else:
        max_col_row = max_row

    # 최종맥스 구하기
    if max_dig > max_col_row:
        ans = max_dig
    else:
        ans = max_col_row
    
    print(f'#{T} {ans}')

    


    
