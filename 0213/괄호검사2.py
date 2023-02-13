import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    code = list(input())
    stack = []
    flag = 1
    for c in code:
        if c == '(' or c == '{':
            stack.append(c)
        else:
            if c == ')':
                if stack != []:
                    top = stack.pop()
                    if top != '(':
                        flag = 0
                        break
                else:
                    flag = 0
                    break
            elif c == '}':
                if stack != []:
                    top = stack.pop()
                    if top != '{':
                        flag = 0
                        break
                else:
                    flag = 0
                    break
    if stack == [] and flag == 1:
        flag = 1
    else:
        flag = 0
    print(f'#{t} {flag}')
