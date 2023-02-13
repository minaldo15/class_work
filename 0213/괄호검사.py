import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    bracket = list(input())
    stack = []
    flag = 1
    for b in bracket:
        if b == '(':
            stack.append(b)
        else:
            if b == ')':
                if stack != []:
                    stack.pop()
                else:
                    flag = 0
                    break
    if stack == [] and flag == 1:
        flag = 1
    else:
        flag = 0
    print(f'#{t} {flag}')
