import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    i = 0
    while True:
        i += 1
        if i > 5:
            i = 1
        data.append(data.pop(0) - i)
        if data[-1] <= 0:
            data[-1] = 0
            break
    print(f'#{t}', *data)
