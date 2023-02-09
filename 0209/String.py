import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
for t in range(10):
    T = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)
    cnt = 0
    for i in range(M, N - M + 1):
        flag = 0
        if t[i] == p[0]:
            for j in range(M):
                if t[i + j] != p[j]:
                    flag = 0
                    break
                else:
                    flag = 1
        if flag == 1:
            cnt += 1
    print(f'#{T} {cnt}')


