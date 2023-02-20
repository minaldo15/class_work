import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []
    for i in range(1, N+1): # 화덕 크기 만큼 피자 넣기
        q.append((i, lst.pop(0)))

    while q:
        n, piz = q.pop(0)
        piz = piz//2
        if piz == 0:
            if lst:
                i += 1
                q.append((i, lst.pop(0)))
        else:
            q.append((n, piz))

    ans = n
    print(f'#{t} {ans}')



