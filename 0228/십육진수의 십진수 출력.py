import sys
sys.stdin = open('input.txt', 'r')
def makeint(a):
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
for tc in range(1, T + 1):
    a = input()
    b = ""
    for num in a:
        if num.isdigit():
            b += f'{int(num):04b}'
        else:
            b += f'{makeint(num):04b}'
    n = len(b)
    alst = []
    for i in range(n//7+1):
        alst.append(int('0b'+b[i*7:i*7+7], 2))
    print(f'#{tc}', *alst)
