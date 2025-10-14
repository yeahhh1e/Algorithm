def solution(a, b):
    a = str(a)
    b = str(b)
    answer = ''

    if int(a + b) >= int(b + a):
        answer = a + b
    elif int(b + a) > int(a + b):
        answer = b + a

    return int(answer)