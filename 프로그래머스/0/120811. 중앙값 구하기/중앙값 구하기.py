def solution(array):
    sorted_array = sorted(array)
    m = len(sorted_array)
    middle = m // 2
    # if m % 2 > 0:
    #     middle += 1
    answer = sorted_array[middle]
    return answer