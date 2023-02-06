import sys
sys.stdin = open('input.txt')

for T in range(1,4):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N - 2):
        if lst[i] > lst[i-1] and lst[i] > lst[i-2]:
            if lst[i] > lst[i+1] and lst[i] > lst[i+2]:
                top = lst[i]                              
                sec = max(lst[i-2],lst[i-1],lst[i+1],lst[i+2])
                cnt += (top - sec)
    print(f'#{T} {cnt}')
