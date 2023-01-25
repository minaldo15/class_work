# fn_d(91) 
# 출력 예시 
# 101
# def fn_d(n):

def sum_n(n): # 각 자릿수 숫자들의 합 구하기
    lst = list(str(n))
    return sum(map(int,lst))
# print(sum_n(5678))

def d(n): #d(n) 정의
    return sum_n(n) + n 

def fn_d(dn):
    for i in range(dn):    
        if d(i) == dn: # generator 있음
            return 'have generator'
    return 'selfnumber'

for i in range(1,32):
    print(i, fn_d(i))
