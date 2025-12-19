def solution(my_string, is_prefix):
    result = 1 
    for i in range(len(is_prefix)):
        if len(is_prefix) > len(my_string):
            result = 0
        elif my_string[i] != is_prefix[i]:
            result = 0
    return result