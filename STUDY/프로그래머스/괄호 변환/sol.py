def solution(p):
    if p == '':
        return

# 균형잡힌 string : 왼오 각각의 총 수가 맞는 것
# 올바른 string: 왼오 짝까지 맞는 것
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. string w를 두 "균형잡힌 괄호 string" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 string"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. string u가 "올바른 괄호 string" 이라면 string v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. string u가 "올바른 괄호 string"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. string v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
# 균형잡힌 string 판별 함수
def balance(p):
    left = 0
    right = 0
    # stack = []
    for i in range(len(p)):
        if i == '(':
            left += 1
        else:
            right += 1
        if left == right: # 짝 맞으면 끊고 u로 만들어주기
            u = p[:i+1]
            v = p[i+1:]
        balance(v)
        print(u, v)
        # if p[i] == '(': # 여는 괄호일 때 스택 추가
        #     stack.append('(')
        # else:           # 닫는 괄호일 때 스택에서 뺀 후 비교
        #     a = stack.pop()
        #     if a == '(': # 마지막에 저장된 요소가 여는 괄호 ->
        #         if len(stack) == 0:
        #             u = p[:i+1]
        #     else: # 마지막에 저장된 요소가 닫는 괄호
        #         pass # 그대로 진행

balance(p)
