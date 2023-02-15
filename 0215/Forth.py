import sys
sys.stdin = open('input.txt', 'r')

def calc(a, b, c):
    op = ['+', '-', '*', '/']
    if c == op[0]:
        return int(a) + int(b)
    elif c == op[1]:
        return int(a) - int(b)
    elif c == op[2]:
        return int(a) * int(b)
    elif c == op[3]:
        return int(a) // int(b)

T = int(input())
for t in range(1, T + 1):
    cal = input().split()
    stk = []
    for c in cal:
        if c.isdigit():
            stk.append(c)
        elif c == '.':
            if len(stk) > 1:
                print(f'#{t} error')
            else:
                print(f'#{t} {stk.pop()}')
        else:
            if stk:
                b = stk.pop()
                if stk:
                    a = stk.pop()
                    stk.append(calc(a, b, c))
                else:
                    print(f'#{t} error')
                    break
            else:
                print(f'#{t} error')
                break





