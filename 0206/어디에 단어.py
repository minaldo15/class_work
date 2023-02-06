import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    for n in range(N):
        arr = list(map(int, input().split()))
        cnt = 0
        for i in range(N):
            if arr[i] == 1:
                cnt += 1 
            else:
                ans = cnt
                cnt = 0
            if ans == K:
                result += 1
                ans = 0
    print(result)
            
           

            

            

                

