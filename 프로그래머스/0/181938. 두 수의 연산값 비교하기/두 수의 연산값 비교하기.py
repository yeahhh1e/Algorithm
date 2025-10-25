def solution(a, b):
    answer = 0
    add_def(a, b)
    if result >= 2 * a * b:
        answer = result
    else:
        answer = 2 * a * b
    
    return answer
def add_def(a, b):
    global result
    a = str(a)
    b = str(b)
    result = 0
    result = int(a + b)