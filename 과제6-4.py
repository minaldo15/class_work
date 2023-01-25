# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = ['eat','tea','tan','ate','nat','bat']
#알파벳 a, e, t / b, a, t 개수 각각 비교

# 딕셔너리 만들기 eat(key값) => e:1개, a:1개, t:1개(value값) 
for word in words:
        sorted_word = sorted(word)
        key = ' '.join(sorted_word)
        print(key)