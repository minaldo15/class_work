import sys
sys.stdin =open('input.txt', 'r')
for t in range(1, 11):
    N, nums = input().split()
    stk = []
    for num in nums:
        if stk:
            if num == stk[-1]:
                stk.pop()
            else:
                stk.append(num)
        else:
            stk.append(num)
    print(f'#{t} {"".join(stk)}')