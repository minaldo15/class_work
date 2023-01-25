Rotten_lst = list(input().split(','))
# lst = 'apple,rottenBanana,Apple,RoTTenorange,Orange'
# Rotten_lst = list(lst.split(','))
fresh_lst = list()
for i in range(len(Rotten_lst)):
    if 'rotten' in Rotten_lst[i].lower():
        fresh_lst.append(Rotten_lst[i][6:].lower())
    else:
        fresh_lst.append(Rotten_lst[i].lower())

print(fresh_lst)

