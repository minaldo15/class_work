import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    ans = 0
    p = '1' * K
    cnt = 0
    for lst in arr:
        new_lst = list(''.join(lst).split('0'))
        cnt += new_lst.count(p)
    arr1 = list(zip(*arr))
    for lst in arr1:
        new_lst = list(''.join(lst).split('0'))
        cnt += new_lst.count(p)

    print(f'#{t} {cnt}')

