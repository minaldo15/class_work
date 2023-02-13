import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    string = list(input())
    stack = []
    for s in string:
        if stack != []:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    print(f'#{t} {len(stack)}')
