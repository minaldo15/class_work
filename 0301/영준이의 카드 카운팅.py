import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    dic = {'S':[],'D':[],'H':[], 'C':[]}
    S = input()
    n = len(S)
    flag = 0
    for i in range(n//3):
        if S[i*3+1:i*3+3] in dic[S[i*3]]:
            print(f'#{tc} ERROR')
            flag = 1
            break
        else:
            dic[S[i*3]].append(S[i*3+1:i*3+3])
    if flag == 0:
        print(f'#{tc} {13-len(dic["S"])} {13-len(dic["D"])} {13-len(dic["H"])} {13-len(dic["C"])}')

