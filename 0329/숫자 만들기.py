import sys
import math
sys.stdin = open('input.txt', 'r')

def cal(a,b,n):
    if n == 0:
        return a+b
    if n == 1:
        return a-b
    if n == 2:
        return a*b
    if n == 3:
        return math.trunc(a/b)

def dfs(i, cnt):
    global MIN, MAX, ans
    alst = lst[:]

    if i==4:
        for l in range(N-1):
            alst[l+1] = cal(alst[l], alst[l+1], op[l])
        cnt = alst[-1]
        MIN = min(MIN, cnt)
        MAX = max(MAX, cnt)
        return
    for j in range(i, 4):
        op[i],op[j] = op[j],op[i]
        dfs(i+1, cnt)
        op[i],op[j] = op[j],op[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_op = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    op = [] # 0:+, 1:-, 2:*, 3:/
    MAX = -100000000
    MIN = 100000000
    for i in range(4):
        for _ in range(num_op[i]):
            op.append(i)
    dfs(0, 0)

    print(f'#{tc} {MAX - MIN}')

