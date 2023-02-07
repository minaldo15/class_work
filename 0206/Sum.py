import sys
sys.stdin = open("input.txt", "r")

for t in range(2):
    T = int(input())
    arr = []
    N = 100
    ans = 0
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    # 행,열 비교
    sum_row = sum_col = 0
    for i in range(N): 
        for j in range(N):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
    if sum_row > ans:
        ans = sum_row
    elif sum_col > ans:
        ans = sum_col       

    # 대각선 비교
    # 우하향
    sum1 = 0
    for k in range(N):
        sum1 += arr[k][k]
    if sum1 > ans:
        ans = sum1
    # 좌하향
    sum2 = 0
    for k in range(N):
        sum2 += arr[k][N - k - 1]
    if sum2 > ans:
        ans = sum2
 
    print(f'#{T} {ans}')

    


    
