def solution(num_list):
    time = 1
    for i in num_list:
        time *= i
    add = sum(num_list)
    add = add * add
    if time < add:
        answer = 1
    else:
        answer = 0
    return answer