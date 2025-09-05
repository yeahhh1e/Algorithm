import sys
sys.stdin = open("input.txt", "r")

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]



M = int(input())
M_list = list(map(int, input().split())) # ['10', '9', '-5', '2', '3', '4', '5', '-10']


cnt = 0
def binary_search(arr, left, right, target):
    if left > right:
        return 0

    mid = (left + right) // 2

    if arr[mid] == target:
        cnt = 1

        l = mid - 1
        while l >= left and arr[l] == target:
            cnt += 1
            l -= 1

        r = mid + 1
        while r <= right and arr[r] == target:
            cnt += 1
            r += 1

        return cnt

    if arr[mid] < target: # 오른쪽 탐색
        return binary_search(arr, mid+1, right, target)

    elif arr[mid] > target: # 왼쪽 탐색
        return binary_search(arr, left, mid-1, target)


for m in M_list:
    print(binary_search(N_list, 0, len(N_list)-1, m), end=" ")