import sys
sys.stdin = open('input.txt')

for T in range(1,4):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N - 2):
        top = lst[i]                              
        lst_low = lst[i-2:i+3]
        del lst_low[2]
        sec = max(lst_low)
        if top - sec > 0:
            cnt += (top - sec)
        else:
            continue


    print(f'#{T} {cnt}')
