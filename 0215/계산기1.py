import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N = int(input())
    cal = input()
    stk = []
    cal_1 = []
    for c in cal:
        if c.isdigit():
            cal_1.append(c)
        else:
            if stk:
                cal_1.append(stk.pop())
                stk.append(c)
            else:
                stk.append(c)
    if stk:
        cal_1.append(stk.pop())
    for c in cal_1:
        if c.isdigit():
            stk.append(c)
        else:
            b = stk.pop()
            a = stk.pop()
            stk.append(int(a) + int(b))
    print(f'#{t} {stk}')
