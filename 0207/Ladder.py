import sys
sys.stdin = open('input.txt', 'r')
T = 3
for t in range(T):
    case = int(input())
    arr = []
    N = 100
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
    for j in range(N):
        if arr[N - 1][j] == 2:
            start = j

    i = N - 1
    j = start  # 숫자가 2인 지점에서 부터 출발
    while i >= 0: 
        if 1 <= j < N-1: # j가 1부터 N - 2까지일 때(맨처음과 맨마지막 줄 제외)
            if arr[i][j-1] == 1: # 왼쪽이랑 비교
                j -= 1
                arr[i][j] = 3 # 지나간길은 3으로 바꿈
            elif arr[i][j+1] == 1: # 오른쪽이랑 비교
                j += 1
                arr[i][j] = 3
            else:
                i -= 1
                arr[i][j] = 3
        else:
            if j == 0: # 맨 첫 줄
                if arr[i][j+1] == 1: # 오른쪽이랑만 비교
                    j += 1
                    arr[i][j] = 3
                else:
                    i -= 1
                    arr[i][j] = 3
            else: # j == N - 1 (맨 마지막 줄)
                if arr[i][j - 1] == 1: # 왼쪽이랑만 비교
                    j -= 1
                    arr[i][j] = 3
                else:
                    i -= 1
                    arr[i][j] = 3
    for j in range(N):
        if arr[0][j] == 3:
            ans = j
    print(f'#{case} {ans}')






