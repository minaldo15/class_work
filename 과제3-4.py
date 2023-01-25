
a, b, c = map(int, input().split())
if a == b == c:
    print('정삼각형')
else:
    if a == b or b == c or c == a:
        print('이등변삼각형')
    elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
        print('직각삼각형')
    else:
        if a >= b + c or b >= a + c or c >= b + a:
            print('삼각형이 아님')
        else:
            print('삼각형') 