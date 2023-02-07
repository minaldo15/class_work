T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dj = [1,0,-1,0]
    di = [0,1,0,-1]
    i = j = dist = 0 # dist는 방향 (우:0, 하:1, 좌:2, 상:3)
    for k in range(1, N*N + 1):
        arr[i][j] = k
        i = i + di[dist]
        j = j + dj[dist]
        # dist = (dist + 1) % 4 # 그냥 1만 더해주면 방향이 4,5,6 ... 0123을 넘어가버림
        if i<0 or j<0 or i>=N or j>=N or arr[i][j] != 0:
            i = i - di[dist]
            j = j - dj[dist]
            dist = (dist + 1) % 4
            i = i + di[dist]
            j = j + dj[dist]
    print(f'#{t}')
    for row in arr:
        print(*row)







