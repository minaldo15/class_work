import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    stk = ['0']
    cnt = 0
    bit = input()
    for b in bit:
        if b != stk[-1]:
            cnt += 1
            stk.append(b)
    print(f'#{t} {cnt}')
