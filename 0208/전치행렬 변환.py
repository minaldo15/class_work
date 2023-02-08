arr = [[1,2,3],[4,5,6],[7,8,9]]
print(arr[0], arr[1], arr[2]) # arr = arr[0], arr[1], arr[2]
print(*arr)
# arr = print(list(zip(arr[0], arr[1], arr[2])))
arr = list(zip(*arr))
print(arr)