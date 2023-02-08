import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    str = list(input())
    for i in range(len(str)):
        if str[i] == 'b':
            str[i] = 'd'
        elif str[i] == 'd':
            str[i] = 'b'
        elif str[i] == 'p':
            str[i] = 'q'
        elif str[i] == 'q':
            str[i] = 'p'
    ans = str[::-1]
    print(f'#{t}', ''.join(ans))











    # ans = str[::-1]
    # print(f'#{t} {ans}')
