import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T + 1):
    n, ans, k_l = int(input()), "yes", []
    arr= [input() for _ in range(n)]
    for i in arr + list(map(lambda x: "".join(x), zip(*arr))):
        print(list(map(lambda x: "".join(x), zip(*arr))))
        k = i.count("#")
        if k:
            k_l.append(k)
            if "#" * k not in i:
                ans = "no"
                break
    if len(set(k_l)) - 1: ans = "no"
    # print(f"#{t} {ans}")