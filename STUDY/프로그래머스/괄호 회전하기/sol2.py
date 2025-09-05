def check_True(s): # 올바른 괄호 문자열인지 체크하는 함수
    global check
    global count
    stack = []
    check = True
    count = 0

    for i in range(len(s)):
        # x = s[i]
        if s[i] == '(' or s[i] == '{' or s[i] == '[': # 여는 괄호라면 stack에 추가
            stack.append(s[i])
        else: # 닫는 괄호라면
            if stack == []: # stack에 담긴 게 없다면 패스
                check = False
                break
            elif s[i] == ')':
                if stack.pop() == '(':
                    pass
                else:
                    check = False
                    break
            elif s[i] == '}':
                if stack.pop() == '{':
                    pass
                else:
                    check = False
                    break
            elif s[i] == ']':
                if stack.pop() == '[':
                    pass
                else:
                    check = False
                    break
            else: # 괄호 짝이 안 맞는다면
                check = False
                break # count = 0이 됨
        
        if check == False: # False면 for문 종료하고 0을 반환
            break
        else:
            continue
    if stack != []: # stack이 비워지지 않았다는 것은 여는 괄호만 있는 것이므로 False로 바꾸고 종료
        check = False
    if check == True:
        count += 1  # True인 상태면 올바른 괄호 문자열이므로 count 1 증가
    return count

# s를 회전하는 함수
def move(s):
    p = s.pop(0) # 첫번째거 떼기
    s.append(p) # 뒤에 붙이기
        

def solution(s):
    list_s = list(s)
    check = True
    answer = 0
    for _ in range(len(list_s)):
        if check == False: # False상태면 바로 종료
            answer = 0
            break
        check_True(list_s)
        answer += count
        move(list_s)

    return answer

print(solution("{(["))