lst_den = []
lst_amt = []
salt_lst = []
while True:
    den, amt = input()
    lst_den.append(den)
    lst_amt.append(amt)
    salt_lst.append(amt*den/100)
    if input() == 'Done':
        total_amt = sum(lst_amt)
        total_den = (sum(salt_lst)/total_amt)*100
        print(total_den, total_amt)
        break