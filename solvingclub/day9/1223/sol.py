import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, 11):
    T = int(input())
    n_list = list(input())

    stack = [] # 연산자를 담을 스택
    new_list = [] # 후위 표기법으로 바꾼 요소들을 담을 리스트
    operator_dict = {'+' : 0, '*' : 1}
    # 중위를 후위로 바꾸기
    for i in range(len(n_list)):
        if n_list[i].isdigit() == True: # 숫자라면
            new_list.append(n_list[i])  # new_list에 추가
            # print(n_list[i])
        elif n_list[i].isdigit() == False: # 숫자가 아닌 연산자라면
            if len(stack) == 0: # 스택이 비어있는 경우
                stack.append(n_list[i]) # 스택에 연산자 추가
            else:   # 스택이 비어있지 않은 경우
                if operator_dict[n_list[i]] > operator_dict[stack[-1]]:
                    stack.append(n_list[i])
                else:
                    a = stack.pop()  # 연산자 우선순위가 높으면 pop하여 new_list에 추가
                    new_list.append(a)
                    stack.append(n_list[i])
        if len(stack) > 0 and i == len(n_list)-1:   # 스택이 비어있지 않고, 순회를 끝까지 했을 경우
            for _ in range(len(stack)): # 남은 스택이 없을 때까지 new_list에 추가
                a = stack.pop()
                new_list.append(a)
    # print(new_list)
    new_stack = []
    for i in range(len(new_list)):
        if new_list[i].isdigit() == True:   # 숫자라면 new_stack에 추가
            new_stack.append(int(new_list[i]))
        elif new_list[i] == '*':
            n2 = new_stack.pop()
            n1 = new_stack.pop()
            b = n1 * n2
            new_stack.append(b)
        elif new_list[i] == '+':    # + 라면
            n2 = new_stack.pop()    # 숫자들을 pop한 후
            n1 = new_stack.pop()
            b = n1 + n2   # 나중에 빼낸 숫자부터 더해준다
            new_stack.append(b)

    print(f'#{tc} {new_stack.pop()}')


    
        