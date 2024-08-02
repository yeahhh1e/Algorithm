arr1 = [0] * 3

arr2= [[0] * 3 for _ in range(2)]   # 2차원 배열 [[0, 0, 0], [0, 0, 0]]
# print(arr1)
# print(*arr1)
# print(arr2)
# for i in range(2):
#     print(*arr2[i])
for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = ' ')
    print()
