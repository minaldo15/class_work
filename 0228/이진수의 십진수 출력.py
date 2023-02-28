import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    n = len(arr)
    ans = []
    for i in range(n//7):
        a = int('0b'+arr[i*7:i*7+7], 2)
        ans.append(a)
    print(f'#{tc}', *ans)
