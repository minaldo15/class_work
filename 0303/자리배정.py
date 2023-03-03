import sys
sys.stdin = open('input.txt', 'r')

C, R = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
si, sj = R - 1, 0
arr[si][sj] = 1
d = 0
k = 2
ni, nj = si, sj
while k <= K:
    ni += di[d]
    nj += dj[d]
    if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 0:
        arr[ni][nj] = k
        k += 1
    else:
        ni -= di[d]
        nj -= dj[d]
        d = (d+1)%4
    if arr[ni][nj] == K:
        ei, ej = ni, nj
if K > C*R:
    print(0)
else:
    ans = (ej+1, si-ei+1)
    print(*ans)








