def check_true(s): # 올바른 괄호 문자열인지 체크하는 함수
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[': # 여는 괄호라면 stack에 추가
            stack.append(s[i])
        else: # 닫는 괄호라면
            if stack == []: # stack에 담긴 게 없다면 패스
                return 0
            elif s[i] == ')':
                if stack.pop() != '(':
                    return 0
            elif s[i] == '}':
                if stack.pop() != '{':
                    return 0
            elif s[i] == ']':
                if stack.pop() != '[':
                    return 0
        
    if stack != []: # stack이 비워지지 않았다는 것은 여는 괄호만 있는 것이므로 False로 바꾸고 종료
        return 0
    else:
		    return 1

# s를 회전하는 함수
def move(s):
    p = s.pop(0) # 첫번째거 떼기
    s.append(p) # 뒤에 붙이기
        
def solution(s):
    list_s = list(s)
    answer = 0
    for _ in range(len(list_s)):
        answer += check_true(list_s)
        move(list_s)

    return answer