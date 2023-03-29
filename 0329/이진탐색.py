import sys
sys.stdin = open('input.txt', 'r')

def binary_search(arr, target, start, end):
    global left, right
    if start > end:
        return None

    # 중간 인덱스는 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스
    # 몫만 구하기 위해 // 연산자 활용
    mid = (start + end) // 2

    # 중간 인덱스의 값이 타겟 데이터와 같은 경우 탐색 종료
    if arr[mid] == target:
        return mid

    # 중간 인덱스의 값이 타겟 데이터보다 큰 경우
    # 마지막 인덱스를 중간 인덱스의 한 칸 앞으로 이동
    elif arr[mid] > target:
        left += 1
        return binary_search(arr, target, start, mid - 1)

    # 중간 인덱스의 값이 타겟 데이터보다 작은 경우
    # 시작 인덱스를 중간 인덱스의 한 칸 뒤로 이동
    else:
        right += 1
        return binary_search(arr, target, mid + 1, end)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for num in B:
        left = 0
        right = 0
        result = binary_search(A, num, 0, N-1)
        print(result, left, right)
        if result != None:
            if left + right < 2:
                cnt += 1
            else:
                if left and right:
                    cnt += 1
    print(f'#{tc} {cnt}')
