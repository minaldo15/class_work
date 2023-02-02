T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    charge.append(N) # 종점을 검증하기 위해
    cnt = 0
    check = 0 # 충전한 장소(0부터 출발)
    for i in range(M):
        if K < charge[0] or K < N - charge[-2]: # 처음과 마지막 충전소 검증
            cnt = 0
            break
        else:
            if (charge[i] - check) <= K and (charge[i+1] - check) > K: 
                check = charge[i]
                cnt += 1
            else:
                if (charge[i] - check) > K:
                    cnt = 0
                    break
    print(f'#{t} {cnt}')




        # else:
        #     if K == charge[i] - check: # 충전한 장소에서 해당 충전소까지 거리가 가용거리와 같을 때
        #         cnt += 1
        #         check = charge[i]
        #     elif K < charge[i] - check: # 충전한 장소에서 해당 충전소까지 거리가 가용거리 초과일 때
        #         if check == charge[i-1]: # 충전한 장소가 이전 충전소이하였을 경우면 종점까지 못감
        #             cnt = 0
        #             break
        #         else:                      
        #             cnt += 1
        #             check = charge[i-1] # 충전한 장소가 이전 충전소가 아니면 이전 충전소에서 충전했으면됨
        #     elif K > charge[i] - check: 
        #         if N - charge[i] <= K:  # 마지막 충전소 카운트 하기
        #             if charge[i] == charge[-1]:
        #                 cnt += 1
        #                 break
                # else: 
                #     continue
                