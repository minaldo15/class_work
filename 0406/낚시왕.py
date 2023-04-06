import sys
sys.stdin = open('input.txt', 'r')

di = [0,-1,1,0,0]
dj = [0,0,0,1,-1]
sharks = []
cnt = 0
time = 0
MAX = 0 # 맥스 스피드
R, C, M = map(int, input().split())
for _ in range(M):
    r, c, s, d, z = map(int, input().split())   # r,c 위치 s 속력, d 방향, z 크기
    sharks.append([r,c,s,d,z])
    if s > MAX:
        MAX = s
sharks.sort()   # 행이(shark[0]) 낮은 순으로 정렬
while time < C:
    time += 1
    # 땅에서 제일 가까운 상어를 잡는다.(같은 열이라도 행이 낮은 순)
    for shark in sharks:
        if shark[1] == time:
            cnt += shark[4]
            shark[:] = [0,0,0,0,0] # 잡힌 것으로 처리
            break
    # 상어들 이동
    sec = 0
    while sec <= MAX:
        sec += 1
        for shark in sharks:
            if shark[2] >= sec:
                shark[0] += di[shark[3]]
                shark[1] += dj[shark[3]]
            if shark[0] < 1:
                shark[0] = 2
                shark[3] = 2
            elif shark[0] > R:
                shark[0] = R - 1
                shark[3] = 1
            if shark[1] < 1:
                shark[1] = 2
                shark[3] = 3
            elif shark[1] > C:
                shark[1] = C - 1
                shark[3] = 4
    # 같은 위치에 있는 상어는 잡아먹어야 되니까 행, 열으로 정렬(그리고 마지막 크기 순으로 정렬: 뒤에 오는 상어의 크기가 큼)
    sharks.sort(key=lambda x:(x[0],x[1],x[4]))
    for i in range(1, M):
        # 현재 상어가 앞에 있는 상어와 위치가 같다면
        if (sharks[i][0], sharks[i][1]) == (sharks[i-1][0], sharks[i-1][1]):
            sharks[i][4] += sharks[i-1][4]  # 크기만 더해줌 방향은 어차피 그대로
            sharks[i-1][:] = [0,0,0,0,0]    # 먹힌상어는 0처리

print(cnt)



