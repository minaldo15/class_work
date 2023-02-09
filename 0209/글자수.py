import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    set1 = set(str1)
    max = 0
    for a in set1:
        cnt = 0
        for b in str2:
            if a == b:
                cnt += 1
        if cnt > max:
            max = cnt
    print(f'#{t} {max}')
