import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = input()
    lst = list(map(int, N))
    n = len(lst)
    max = min = int(N)
    for i in range(n):
        for j in range(i, n):
            tmp = lst[:]
            tmp[i], tmp[j] = tmp[j], tmp[i]
            if tmp[0] != 0:
                new_N = 0
                k = 0
                t = n - 1
                while t>=0:
                    new_N += tmp[t] * (10**k)
                    k += 1
                    t -= 1
                if new_N > max:
                    max = new_N
                if new_N < min:
                    min = new_N
    print(f'#{tc} {min} {max}')
