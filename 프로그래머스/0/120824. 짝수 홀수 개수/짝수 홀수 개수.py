def solution(num_list):
    n = 0
    m = 0
    for i in num_list:
        if i % 2 == 0:
            n += 1
        else:
            m += 1
    answer = [n, m]
    return answer