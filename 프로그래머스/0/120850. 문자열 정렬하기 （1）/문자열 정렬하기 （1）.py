def solution(my_string):
    answer = []
    for i in my_string:
        try:
            if i.isdigit() == True:
                answer.append(int(i))
        except ValueError:
            pass
    answer = sorted(answer)
    return answer