import sys
sys.stdin = open('input.txt', 'r')

for _ in range(4):
    lst = list(map(int,input().split()))
    x1, y1, p1, q1 = lst[0], lst[1], lst[2], lst[3]
    x2, y2, p2, q2 = lst[4], lst[5], lst[6], lst[7]
    if x2 > p1 or x1 > p2 or y2 > q1 or y1 > q2:
        ans = 'd'
    elif p1 == x2:
        if q2 > y1 and q1 > y2:
            ans = 'b'
        else:
            if q2 == y1 or q1 == y2:
                ans = 'c'
    elif p2 == x1:
        if q1 > y2 and q2 > y1:
            ans = 'b'
        else:
            if q2 == y1 or q1 == y2:
                ans = 'c'
    elif q1 == y2:
        if p2 > x1 and p1 > x2:
            ans = 'b'
        else:
            if p2 == x1 or p1 == x2:
                ans = 'c'
    elif q2 == y1:
        if p1 > x2 and p2 > x1:
            ans = 'b'
        else:
            if p1 == x2 or p2 == x1:
                ans = 'c'
    else:
        ans = 'a'
    print(ans)


