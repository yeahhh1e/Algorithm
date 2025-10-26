def solution(n):
    answer = 0
    check = n ** 0.5
    if check % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer