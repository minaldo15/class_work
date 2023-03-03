import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "yes"
    stk = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                stk.append((i,j))
    si, sj = stk[0]
    ei, ej = stk[-1]
    if si - ei != sj - ej:
        ans = "no"
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if arr[i][j] == '.':
                ans = "no"
                break
    print(f'#{tc} {ans}')
