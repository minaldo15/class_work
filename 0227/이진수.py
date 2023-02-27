import sys
sys.stdin = open('input.txt', 'r')

def makenum(a):
    if a == 'A':
        return 10
    elif a == 'B':
        return 11
    elif a == 'C':
        return 12
    elif a == 'D':
        return 13
    elif a == 'E':
        return 14
    elif a == 'F':
        return 15

T = int(input())
for t in range(1, T + 1):
    N, bit16 = input().split()
    bit2 = ""
    N = int(N)
    for i in bit16:
        if i.isdigit():
            bit2 += f'{int(i):04b}'
        else:
            bit2 += f'{makenum(i):04b}'

    print(f'#{t} {bit2}')
