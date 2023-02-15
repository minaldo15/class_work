import sys
sys.stdin = open('input.txt', 'r')

op = ['+', '*']
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    arr = list(input())
    stk = []
    for a in arr:
        if a not in op:
            print(a, end='')
        else:
            if stk:
                if op.index(stk[-1]) < op.index(a):
                    stk.append(a)
                else:
                     while True:
                         print(stk.pop(), end='')
                         if stk == [] or op.index(stk[-1]) < op.index(a):
                            stk.append(a)
                            break

            else:
                stk.append(a)

    while stk:
        print(stk.pop(), end='')
    print()



