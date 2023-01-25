import random

lst = [
    '고영진','구본웅','김성용','김하늘','김하림',
    '김현아','민경현','배이경','서동훈','송준우',
    '심현재','유창재','윤민영','윤태영','이민호',
    '이성섭','이성우','이영아','이예슬','임수형',
    '임혜진','정선재','정현아','진익근','최태호',
    '최홍준','하정호','허주혁'
]


group = []
n = int(input())
for i in range(len(lst)//n):
    if len(lst) >= n:
        team = random.sample(lst, n)
        group.append(team)
        for name in team:
            if name in lst:
                lst.remove(name)
    else:
        break
        
print(group)
