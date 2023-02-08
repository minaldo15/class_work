import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for n in range(N):
        lst = list(input())
        arr.append(lst)
    # print(arr)
    # 가로(행) 검증
    flag = 0
    for lst in arr:
        for i in range(N - M + 1):
            if lst[i:i+M] == lst[i:i+M][::-1]:
                ans = lst[i:i+M]
                flag = 1
                break
        if flag == 1:
            break

    # 세로(열) 검증
    # 전치행렬로 바꿔줌
    arr = list(zip(*arr))
    for lst in arr:
        for i in range(N - M + 1):
            if lst[i:i + M] == lst[i:i + M][::-1]:
                ans = lst[i:i + M]
                flag = 1
                break
        if flag == 1:
            break
    print(f'#{t}', ''.join(ans))





