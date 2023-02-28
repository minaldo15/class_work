import sys
sys.stdin = open('input.txt', 'r')

def makeint(a):
    if a == 'A':
        return 10
    elif a == 'B':
        return 11
    elif a == 'C':
        return 12
    elif a == 'D':
        return 13
    elif a == 'E':
        return 14
    elif a == 'F':
        return 15

dic = {'001101':0, '010011':1, '111011':2, '110001':3, '100011':4, '110111':5, '001011':6, '111101':7, '011001':8, '101111':9}

T = int(input())
for tc in range(1, T + 1):
    a = input()
    b = ""
    for num in a:
        if num.isdigit():
            b += f'{int(num):04b}'
        else:
            b += f'{makeint(num):04b}'
    n = len(b)
    alst = [dic[b.rstrip('0')[-6:]]]    # 맨 마지막 코드의 암호 넣어둠
    i = 1
    while True:
        code = b.rstrip('0')[-i*6-6:-i*6]   # 뒤에서 부터 6개씩 짤라서 코드입력 받음
        if code in dic: # 코드가 암호 딕셔너리에 있다면
            alst.insert(0, dic[code])
        i += 1
        if i == n//6:
            break
    print(f'#{tc}', *alst)


