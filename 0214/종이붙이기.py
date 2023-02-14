import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    n = N//10
    lst = [0]*n
    lst[0] = 1
    lst[1] = 3
    for i in range(2, n):
        lst[i] = lst[i-1] + lst[i-2]*2
    ans = lst[n - 1]

    print(f'#{t} {ans}')
