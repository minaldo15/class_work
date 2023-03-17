import sys
sys.stdin=open('input.txt','r')

def danjo(n):
    flag = 0
    number = str(n)
    for i in range(1, len(number)):
        if number[i]>=number[i-1]:
            pass
        else:
            flag = 1
            break
    return flag

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Alst = list(map(int, input().split()))
    max = -1
    for i in range(N):
        for j in range(i+1, N):
            num = Alst[i]*Alst[j]
            if danjo(num) == 0:
                ans = num
                if ans > max:
                    max = ans
    print(f'#{tc} {max}')
