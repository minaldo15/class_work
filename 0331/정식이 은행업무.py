import sys
sys.stdin = open('input.txt','r')

def dfs(i, k, num, lst, n):
    if i == k:
        return
    for j in range(1, n):   # 한개 이상은 틀렸으니 0부터(원상태)가 아닌 1부터
        num[i] = (num[i]+j)%n # 3진법일 경우 2에서 1로 바뀌려면 (2+2)%3
        lst.append(int(''.join(map(str,num)), n))
        num[i] = (num[i]-j)%n # 원상복구
    dfs(i+1, k, num, lst, n)

T = int(input())
for tc in range(1, T+1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))
    lst2 = []
    lst3 = []
    dfs(0, len(num2), num2, lst2, 2)
    dfs(0, len(num3), num3, lst3, 3)
    for num in lst2:
        if num in lst3:
            ans = num
            break
    print(f'#{tc} {ans}')
