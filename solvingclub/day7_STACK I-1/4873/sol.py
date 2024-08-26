import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    s = input()
    
    size = len(s)
    stack = []    # stack 만들기

    for i in range(0, size):
        stack.append(s[i])  # 스택에 요소 넣기
        if len(stack) > 1:  # 요소가 두 개 이상 있을 경우에만 반복 검사
            if stack[-1] == stack[-2]:  # 방금 넣은 요소와 전에 넣은 요소가 같으면
                stack.pop()             # 둘 다 스택에서 빼기
                stack.pop()

    print(f'#{test_case} {len(stack)}')
            