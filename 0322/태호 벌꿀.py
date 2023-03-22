import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    alst = []
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            hc = 0
            lst = []
            cnt1 = 0
            for k in range(j,j+M):
                hc += arr[i][k]
                lst.append(arr[i][k])        # 리스트에  일꾼 한명이 캘수 있는 수를 넣어서
            if hc <= C:                         # 그수 의 합이 c보다 작으면
                for l in range(len(lst)):
                    cnt += lst[l] ** 2
                alst.append(cnt)           # 다 제곱해서 더해서 alst 에 넣고

            else:                  # 그 값이 c 보다 크면
                lst.sort()       #솔트하고
                print(lst)
                lst1 = []
                while 1:                  # 반복할건데
                    b = lst.pop(0)    # 작은수부터 뺼거야
                    lst1.append(b)      # 그 수는 따로 모으고
                    a = sum(lst)     # 빼서 그수가 c보다 작으면 멈춰라
                    if a <= C:
                        break

                for l in range(len(lst)):     # 이거는 그냥 멈추자마자 바로 제곱해서 값을 더하고
                    cnt += lst[l] ** 2
                lst.pop(0)                     # 이걸 왜햇는지 모르겟어

                lst1.pop()                         # 마지막은  c보다 커서  lst에서뺸것이기떄문에  lst1에서 하나 뺌
                for l in range(len(lst1)-1,-1,-1):   # 뺀수중 큰 수부터 다시 더해서 들어갈거야
                    lst.append(lst1[l])
                    if sum(lst) > C:
                        lst.pop()


                for l in range(len(lst)):   # 다시 들어간 것들의 합을 구한다
                    cnt1 += lst[l] **2
                if cnt < cnt1:
                    cnt = cnt1
                alst.append(cnt)
        print(lst)
    # alst 는 각 자리에서 구할 수 있는 최대 값이 나온다
    # 문제가  이 위에서 발생생


    #밑에 식은  alst 에서 이 가장 최대값을 구하고  그옆으로 겹치는 자리의 값을 뺴버리는 공식이다
    mx = max(alst)
    clst = []
    for i in range(len(alst)):
        if alst[i]== mx:
            a = i // (N-M+1)
            b = i % (N-M+1)
    clst = alst[a*(N-M+1):(a+1)*(N-M+1)]
    dlst = []
    for i in range(1,M):
        c = b-i
        e = b+i
        if 0<=c <len(clst):
            dlst.append(clst[c])
        if 0<= e < len(clst):
            dlst.append(clst[e])

    alst.sort()
    dlst.sort()
    # print(dlst)
    if dlst:
        while 1:
            if alst[-2] == dlst[-1]:
                alst.pop(-2)
                dlst.pop()
                if not dlst:
                    break
            else:
                break
    else:
        pass
    # print(alst)

    ans = alst[-1]+alst[-2]
    print(f'#{t} {ans}')