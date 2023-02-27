import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = float(input())
    stk = []
    k = 1
    while N > 0:
        if N >= 1/2**k:
            stk.append(1)
            N -= 1/2**k
        else:
            stk.append(0)
        k += 1
    if len(stk) < 13:
        print(f'#{t}', end = ' ')
        print(*stk, sep='')
    else:
        print(f'#{t} overflow')


