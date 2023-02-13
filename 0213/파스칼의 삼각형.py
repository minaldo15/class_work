import sys
sys.stdin = open('input.txt', 'r')

def pascal(N):
    lst = []
    if N == 1:
        return [1]
    elif N == 2:
        return [1,1]
    else:
        lst.append(1)
        for i in range(len(pascal(N-1)) - 1):
            lst.append(pascal(N - 1)[i] + pascal(N - 1)[i+1])
        lst.append(1)
        return lst


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    for n in range(1, N + 1):
        print(*pascal(n))

