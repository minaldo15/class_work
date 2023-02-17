import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    stk = []
    profit = []
    while True:
        if stk:
            if price[-1] > stk[-1]:
                stk.append(price.pop())
            else:
                profit.append(stk[-1] - price.pop())
        else:
            stk.append(price.pop())
        if price == []:
            break
    ans = sum(profit)
    print(f'#{t} {ans}')

