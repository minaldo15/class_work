import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    total = []
    for n in range(N):
        C, K = input().split()
        for k in range(int(K)):
            total.append(C)

    print(f'#{t}')
    count = 0
    for i in total:
        print(i,end='')
        count += 1
        if count == 10:
            print('')
            count = 0
    print()





