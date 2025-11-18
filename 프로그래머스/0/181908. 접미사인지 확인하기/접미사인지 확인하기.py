def solution(my_string, is_suffix):
    answer = 0
    if is_suffix in my_string:
        if is_suffix == my_string[-len(is_suffix):]:
            answer = 1
        else:
            answer = 0
    return answer