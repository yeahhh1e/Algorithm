def solution(hp):
    a = hp // 5
    hp -= 5*a
    b = hp // 3
    hp -= 3*b
    c = hp
    answer = a+b+c
    return answer