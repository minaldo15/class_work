import sys
sys.stdin=open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0]*N for _ in range(N)]
    arr_270 = [[0]*N for _ in range(N)]
    arr = []
    for n in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N-1-j][i]

    print(f'#{t}')
    for n in range(N):
            print(''.join(map(str, arr_90[n])), ''.join(map(str, arr_180[n])), ''.join(map(str, arr_270[n])))

