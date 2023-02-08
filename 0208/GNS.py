import sys
sys.stdin = open('input.txt', 'r')

def num(string):
    if string == 'ZRO':
        return 0
    elif string == 'ONE':
        return 1
    elif string == 'TWO':
        return 2
    elif string == 'THR':
        return 3
    elif string == 'FOR':
        return 4
    elif string == 'FIV':
        return 5
    elif string == 'SIX':
        return 6
    elif string == 'SVN':
        return 7
    elif string == 'EGT':
        return 8
    elif string == 'NIN':
        return 9

T = int(input())
for t in range(T):
    case, N = input().split()
    lst = list(input().split())
    count = [0]*10
    s_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for s in lst:
        count[num(s)] += 1

    ans = []
    for i in range(10):
        for _ in range(count[i]):
            ans.append(s_lst[i])

    print(case)
    print(*ans)




