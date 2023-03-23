import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    tickets = list(map(int, input().split()))   # 하루:0, 한달:1, 세달:2, 일년:3
    plans = list(map(int, input().split()))
    costs =[0]*12
    costs[0] = min(tickets[0]*plans[0], tickets[1])
    costs[1] = costs[0] + min(tickets[0]*plans[1], tickets[1])
    costs[2] = min(costs[1] + min(tickets[0]*plans[2], tickets[1]), tickets[2])
    for i in range(3, 12):
        #   i 가 3이라면 costs[0]에 3개월 이용권을 더한 것과 costs[2]에 한달(하루, 한달 이용권 비교)의 비용을 더한 것을 비교
        costs[i] = min(costs[i-3] + tickets[2], costs[i-1] + min(tickets[0]*plans[i], tickets[1]))
    # 마지막 달은 1년 이용권과 비교
    costs[11] = min(costs[11], tickets[3])
    print(f'#{tc} {costs[11]}')