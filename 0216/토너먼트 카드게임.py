import sys
sys.stdin = open('input.txt', 'r')

def solve(i, j):
    if i == j:
        return i

    a = solve(i, (i+j)//2)
    b = solve((i + j)//2 + 1, j)
    if (lst[a] % 3) + 1 == lst[b]:
        return b
    else:
        return a

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    ans = solve(1, N)
    print(f'#{t} {ans}')
