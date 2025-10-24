def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    odd = int(''.join(odd))
    even = int(''.join(even))
    answer = odd + even
    
    return answer