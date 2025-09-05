N = int(input())
N_list = list(input().split())

M = int(input())
M_list = list(input().split()) # 1, 3, 7, 9, 5

N_list.sort() # 1, 2, 3, 4, 5

def binary_search(arr, left, right, target):
    mid = (left + right) // 2
    if (left > right):
        return 0

    if arr[mid] == target:
        return 1

    elif arr[mid] < target:
        return binary_search(arr, mid+1, right, target)

    elif arr[mid] > target:
        return binary_search(arr, left, mid-1, target)


left = 0
right = len(N_list)-1

for m in M_list:
    print(binary_search(N_list, left, right, m))