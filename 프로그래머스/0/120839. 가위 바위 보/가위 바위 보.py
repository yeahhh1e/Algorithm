def solution(rsp):
    list_answer = []
    list_rsp = list(rsp)
    for i in list_rsp:
        if i == "2":
            list_answer.append("0")
        elif i == "0":
            list_answer.append("5")
        else:
            list_answer.append("2")
    
    answer = ''.join(list_answer)
    return answer