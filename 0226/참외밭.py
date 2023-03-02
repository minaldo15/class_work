import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
stk = []
for _ in range(6):
    di, n = map(int, input().split())
    stk.append(n)

i = stk.index(max(stk))
if stk[i+1]>stk[i-1]:
    empty = (stk[i+1] - stk[i-1]) * (stk[i] - stk[i+2])
    sec = stk[i+1]
else:
    empty = (stk[i-1] - stk[i+1]) * stk[i+2]
    sec = stk[i-1]
ans = (stk[i]*sec - empty) * K
print(ans)
