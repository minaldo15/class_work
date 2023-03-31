import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    costs = list(map(int,input().split()))
    plans = list(map(int,input().split()))
    fee = [0]*12
    fee[0] = min(costs[0]*plans[0], costs[1])   # 하루요금과 한달요금 비교
    fee[1] = fee[0] + min(costs[0]*plans[1], costs[1])
    fee[2] = min(fee[1] + min(costs[0]*plans[2], costs[1]), costs[2])   # 세달째에는 각 달의 요금합친것과 세달요금 비교
    for i in range(3, 12):
        # i가 3이라면 fee[3] == (fee[2]에서 한달요금더한 값) vs (fee[0]에 3개월치 요금을 더한값) 중 작은 값
        fee[i] = min(fee[i-1] + min(costs[0]*plans[i], costs[1]), fee[i-3] + costs[2])
    fee[11] = min(fee[11], costs[3])    # 마지막으로 1년치 요금과 비교
    print(f'#{tc} {fee[11]}')
