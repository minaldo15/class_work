import sys
sys.stdin = open('input.txt', 'r')

def check(lst):
    cnt = 0
    # [0:3] 또는 [3:6] 값이 run, tri
    for i in range(0,6,3):
        if lst[i] == lst[i+1] == lst[i+2] or lst[i]+2 == lst[i+1]+1 == lst[i+2]:
            cnt += 1
    return cnt==2
def dfs(i, tlst):
    global ans
    if ans:
        return
    if i == 6:
        if check(tlst):
            ans = 1
        return
    for j in range(6):
        if v[j] == 0:
            v[j] = 1
            dfs(i+1, tlst+[A[j]])
            v[j] = 0


T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input()))
    v = [0]*6
    ans = 0
    tlst = []
    dfs(0, tlst)
    print(f'#{tc} {ans}')



