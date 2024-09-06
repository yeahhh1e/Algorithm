import sys
sys.stdin = open("sample_input.txt", "r")

def merge_sort(n_list):
    global cnt

    if len(n_list) == 1:
        return n_list

    mid = len(n_list) // 2
    left = n_list[:mid]
    right = n_list[mid:]


    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)

def merge(left, right):
    l = r = 0
    result = [0] * (len(left) + len(right))
    # global cnt
    # cnt = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]: # 오른쪽이 더 크다면 왼쪽 먼저 배치
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 5
    n_list = list(map(int, input().split())) # [2, 2, 1, 1, 3]
    cnt = 0

    arr = merge_sort(n_list)

    print(f"#{tc} {arr[N//2]} {cnt}")
