import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    check = [{'W':0, 'B':0, 'R':0} for _ in range(N)]
    for i in range(N):
        check[i]['W'] = arr[i].count('W')
        check[i]['B'] = arr[i].count('B')
        check[i]['R'] = arr[i].count('R')
    min = M*N
    for w in range(N-2):
        for b in range(w+1, N-1):
            ans = 0
            for i in range(w+1):
                ans += (M - check[i]['W'])
            for j in range(w+1, b+1):
                ans += (M - check[j]['B'])
            for k in range(b+1, N):
                ans += (M - check[k]['R'])
            if ans < min:
                min = ans
    print(f'#{tc} {min}')
