import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    flag = 0
    for i in range(M- N + 1):
        if str1 == str2[i:i+N]:
            flag = 1
    print(f'#{t} {flag}')

