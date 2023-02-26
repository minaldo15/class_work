import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
check = {0:5, 1:3, 2:4, 5:0, 3:1, 4:2}
stk = []
for _ in range(N):
    dice = list(map(int, input().split()))
    if stk:
        t = max(stk[-1])
        i = check[stk[-1].idex(t)]
        stk[-1]
    else:
        stk.append(dice)