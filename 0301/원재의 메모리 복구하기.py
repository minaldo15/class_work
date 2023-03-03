import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    stk = ['0']
    N = input()
    cnt = 0
    for i in N:
        if i != stk[-1]:
            cnt += 1
            stk.append(i)
    print(f'#{tc} {cnt}')
