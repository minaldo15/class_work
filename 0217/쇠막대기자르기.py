import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    bar = input()
    stk = []
    check = [] # 레이저인지 체크
    cnt = 0
    for b in bar:
        if check:
            if b == check[-1]:
                stk.append(check.pop())
                check.append(b)
            else:
                cnt += len(stk)
                check.clear()
        else:
            if b == '(':
                check.append(b)
            else:
                if stk:
                    stk.pop()
                    cnt += 1
    print(f'#{t} {cnt}')
