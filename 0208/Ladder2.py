import sys
sys.stdin = open('input.txt', 'r')
T = 1
for t in range(T):
    case = int(input())
    arr = []
    N = 8
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    ladders = []
    j_cnt = {}  # 각 사다리(j)에 대해서 출발지 까지 이동한 횟수 딕셔너리
    for ladder in range(N):
        if arr[N-1][ladder] == 1:
            ladders.append(ladder)
    for ladder in ladders: # 각 사다리들에 대하여 탐색 시작
        arr_1 = [[0]*N for _ in range(N)] # 각 사다리를 탐색 할 때 배열 다시 원위치 (3으로 바꾼거 다시 1로 초기화)
        for i in range(N):
            for j in range(N):
                arr_1[i][j] = arr[i][j]
        cnt = 0
        i = N - 1  # 모든 도착지점에서 부터 위로 올라감
        j = ladder # 도착지점의 j
        while i > 0:
            if 1 <= j < N-1: # j가 1부터 N - 2까지일 때(맨처음과 맨마지막 줄 제외)
                cnt += 1
                if arr_1[i][j-1] == 1: # 왼쪽이랑 비교
                    j -= 1
                    arr_1[i][j] = 3 # 지나간길은 3으로 바꿈
                elif arr_1[i][j+1] == 1: # 오른쪽이랑 비교
                    j += 1
                    arr_1[i][j] = 3
                else:
                    i -= 1
                    arr_1[i][j] = 3
            else:
                if j == 0: # 맨 첫 줄
                    cnt += 1
                    if arr_1[i][j+1] == 1: # 오른쪽이랑만 비교
                        j += 1
                        arr_1[i][j] = 3
                    else:
                        i -= 1
                        arr_1[i][j] = 3
                else: # j == N - 1 (맨 마지막 줄)
                    cnt += 1
                    if arr_1[i][j - 1] == 1: # 왼쪽이랑만 비교
                        j -= 1
                        arr_1[i][j] = 3
                    else:
                        i -= 1
                        arr_1[i][j] = 3
        if i == 0:
            j_cnt[j] = cnt
    lst_min = [k for k, v in j_cnt.items() if min(j_cnt.values()) == v] # cnt가 최소값인 j리스트
    ans = max(lst_min) # j 중에 최댓값
    print(f'#{case} {ans}')

