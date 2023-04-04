import sys
sys.stdin = open('input.txt','r')
import math

di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = []
    time = 0
    ans = 0
    for _ in range(K):
        y, x, n, d = map(int, input().split())
        lst.append([y,x,n,d])
    while time < M:
        for bugs in lst:
            if bugs[0] != -1:   # 먹힌 벌레는 계산 안하기 위해
                bugs[0] += di[bugs[3]]
                bugs[1] += dj[bugs[3]]
                if bugs[0] == 0 or bugs[0] == N-1 or bugs[1] == 0 or bugs[1] == N-1:
                    if bugs[3] == 1 or bugs[3] == 3:
                        bugs[3] += 1
                    elif bugs[3] == 2 or bugs[3] == 4:
                        bugs[3] -= 1
                    bugs[2] = math.floor(bugs[2]/2)
        lst.sort(key=lambda x:(x[0],x[1],x[2])) # 벌레가 많은 군집이 뒤로감
        for i in range(1, len(lst)):
            if lst[i][:2] == lst[i-1][:2]:
                lst[i][2] += lst[i-1][2]
                # lst[i][3] = lst[i][3] # 방향은 바꿔줄 필요없음(벌레가 더많은 군집이 흡수했기 때문에 방향은 그대로)
                lst[i-1][0] = -1        # 먹힌 군집은 -1 처리(계산 안하기 위해)
        time += 1
    for bugs in lst:
        if bugs[0] != -1:
            ans += bugs[2]
    print(f'#{tc} {ans}')
