# arr = [[1, 2, 3], [4, 5, 6]]
# print(len(arr)) # 2 # 배열 수 출력
# print(len(arr[0]))  # 3 # 배열 안 요소의 수 출력

# 쓰지 말기 !
arr = [[0] * 3] * 2
print(arr)

arr[0][0] = 1
print(arr)

"""
"""

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i]= arr[j][i], arr[i][j]

