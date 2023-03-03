import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
di = [0,0,0,1,-1]
dj = [0,1,-1,0,0]
arr = [[0]*1000 for _ in range(1000)]
si,sj = 500, 500
ci, cj = si, sj
for _ in range(6):
    d, n = map(int, input().split())
    ni,nj = ci+di[d]*n, cj+dj[d]*n
    arr[ni][nj] = 1
    ci, cj = ni, nj
stk = []
for i in range(1000):
    for j in range(1000):
        if arr[i][j] == 1:
            stk.append((i, j))
area = (stk[1][1] - stk[0][1])*(stk[2][0] - stk[1][0]) + (stk[5][1] - stk[4][1])*(stk[4][0] - stk[3][0])
ans = area*K
print(ans)