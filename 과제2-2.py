orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# 1. 총 몇잔
# print(len(orders.split(',')))
# 2. 중복메뉴 제거(내림차순 정렬)
pre_orders = orders.split(',')
set_orders = list()
for i in range(len(pre_orders)):
    if pre_orders[i] in set_orders:
        continue
    else:
        set_orders.append(pre_orders[i])
# pre_orders = set(pre_orders)
# pre_orders = sorted(pre_orders, reverse=True)
set_orders.sort(reverse = True)
print(set_orders)