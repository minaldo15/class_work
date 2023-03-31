import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global ans
    if (n+int(''.join(lst))*100) in dct:
        return
    dct[n+int(''.join(lst))*100] = 1

    if n == c:
        ans = max(ans, int(''.join(lst)))
        return
    for i in range(N-1):
        for j in range(i+1, N):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(n+1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    number, c = input().split()
    c = int(c)
    lst = list(number)
    N = len(number)
    ans = 0
    dct = {}
    dfs(0)
    print(f'#{tc} {ans}')
