import sys
sys.stdin = open('input.txt', 'r')

def makenum(n):
    if n == '0001101':
        return 0
    elif n == '0011001':
        return 1
    elif n == '0010011':
        return 2
    elif n == '0111101':
        return 3
    elif n == '0100011':
        return 4
    elif n == '0110001':
        return 5
    elif n == '0101111':
        return 6
    elif n == '0111011':
        return 7
    elif n == '0110111':
        return 8
    elif n == '0001011':
        return 9

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().rstrip('0') for _ in range(N)]
    for lst in arr:
        if lst:
            code = lst
    stk = []
    k = 7
    test = code[-7:]    # 맨뒤에 있는 검증코드
    stk.append(makenum(test))
    for i in range(1, 8):
        num = code[-i*7-7:-i*7]
        stk.append(makenum(num))
    stk.reverse()   # 뒤에서부터 어펜드했기 때문에 뒤집어줌
    total = ((stk[0] + stk[2] + stk[4] + stk[6])*3) + (stk[1] + stk[3] + stk[5]) + stk[7]
    if total % 10 == 0:
        ans = sum(stk)
    else:
        ans = 0
    print(f'#{t} {ans}')

        



                    

                    





