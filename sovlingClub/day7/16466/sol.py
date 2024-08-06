import sys
sys.stdin = open("input.txt", "r")

# 이 문제에서 고려해야 되는 error case
# 1. 괄호가 세트가 아닐 때
# 2. 리스트를 다 순회했는데 괄호가 남아있을 때
# 3. 처음부터 닫는 괄호가 나올 때

T = int(input())
for test_case in range(1, T + 1):
    N = list(input())

    stack = []
    result = 1
    cnt = 0

    for i in range(len(N)):
        cnt += 1
        if N[i] == '{' or N[i] == '(':
            stack.append(N[i])
        elif N[i] == '}':  # } 인 경우
            if len(stack) == 0:
                result = 0
            else:
                a = stack.pop()
                if a != '{':  # { 이 아닌 경우 결과값 0으로 바꿈
                              # 나는 처음에 a = { 인 경우에만 stack에서 pop하는 방법을 사용했는데
                              # 이러면 예외 케이스에 걸리므로 pop 을 먼저 한 후 != 로 비교하는 것이 낫다
                    result = 0

        elif N[i] == ')':  # ) 인 경우
            if len(stack) == 0:
                result = 0
            else:
                a = stack.pop()
                if a != '(':  # ( 이 아닌 경우 결과값 0으로 바꿈
                    result = 0

    if len(stack) > 0: # 스택이 남아 있는 경우 결과값 0
        result = 0

    print(f'#{test_case} {result}')
