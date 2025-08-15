N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

def lower_bound(arr, target, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] < target:
        return lower_bound(arr, target, mid + 1, right)
    else:
        return lower_bound(arr, target, left, mid)

def upper_bound(arr, target, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] <= target:
        return upper_bound(arr, target, mid + 1, right)
    else:
        return upper_bound(arr, target, left, mid)

for m in M_list:
    lb = lower_bound(N_list, m, 0, len(N_list))
    ub = upper_bound(N_list, m, 0, len(N_list))
    print(ub - lb, end=" ")