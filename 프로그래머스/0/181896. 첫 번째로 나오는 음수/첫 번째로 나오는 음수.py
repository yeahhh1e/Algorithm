def solution(num_list):
    answer = 0
    check = False
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            check = True
            break
    if check == False:
        answer = -1
    return answer