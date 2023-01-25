# number = int(input())
# 1. 세로로 출력
# for i in range(number):
#     print(i+1)

# 2. 가로로 출력
# lst_number = list(range(1, number + 1))
# for i in range(len(lst_number)):
#     print(lst_number[i], end=' ')

# print(list(range(1,number+1)))

# 3. 거꾸로 세로로 출력
# for i in range(number + 1):
#     print(number - i)

# 4. 거꾸로 가로로 출력
# lst_number = list(range(number + 1))
# for i in range(len(lst_number)):
#     print(lst_number[number-i], end = ' ')

# 5. N줄 덧셈
# print(sum(list(range(1, number + 1))))

# 6. 삼각형 출력하기
# for i in range(1,number + 1):
#     print(' '*(number - i),'*'*i)

# 7. 중간값 찾기
# numbers = [85, 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67,
# 51, 61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64,
# 52, 90 , 60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24]
# numbers.sort()
# mid_num = numbers[len(numbers)//2]
# print(mid_num)
