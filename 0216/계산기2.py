import sys
sys.stdin = open('input.txt', 'r')

op = ['+', '*']
for t in range(1,11):
    N = int(input())
    cal = input()
    cal1 = []
    stk = []
    for c in cal:
        if c.isdigit():
            cal1.append(c)
        else:
            if stk:
                if op.index(c) > op.index(stk[-1]):
                    stk.append(c)
                else:
                    while True:
                        cal1.append(stk.pop())
                        if stk == [] or op.index(c) > op.index(stk[-1]):
                            stk.append(c)
                            break
                        else:
                            continue
            else:
                stk.append(c)

    while stk:
        cal1.append(stk.pop())

    for c in cal1:
        if c.isdigit():
            stk.append(c)
        else:
            b = int(stk.pop())
            a = int(stk.pop())
            if c == '+':
                stk.append(a+b)
            else:
                stk.append(a*b)

    print(f'#{t}', *stk)
