import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = 0  # 빙고없음
    # 가로검증
    for lst in arr:
        cnt = 0
        if flag == 1:
            break
        for i in range(N):
            if lst[i] == 'o':
                cnt += 1
                if cnt >= 5:
                    flag = 1
                    break
            else:
                cnt = 0
    # 전치행렬, 세로검증
    arr1 = list(zip(*arr))
    if flag == 0:
        for lst in arr1:
            cnt = 0
            if flag == 1:
                break
            for i in range(N):
                if lst[i] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        flag = 1
                        break
                else:
                    cnt = 0

    if flag == 0:
    # 우하향 대각선 (왼쪽위 모서리구간에 오목이 있다면)
        for i in range(N-4): # 우하향 대각선으로 내려갔을때 오목이 5개 이상 있을 수 있는 범위
            for j in range(N-4):
                if arr[i][j] == 'o':
                    for k in range(1, 5):
                        if arr[i+k][j+k] != 'o':
                            break
                    else:
                        flag = 1


    if flag == 0:
        # 좌하향 대각선 (오른쪽위 모서리구간에 오목이 있다면)
        for i in range(N - 4): # 좌하향 대각선으로 내려갔을때 오목이 5개 이상 있을 수 있는 범위
            for j in range(4, N):
                if arr[i][j] == 'o':
                    for k in range(1, 5):
                        if arr[i+k][j-k] != 'o':
                            break
                    else:
                        flag = 1
    if flag == 1:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{t} {ans}')
