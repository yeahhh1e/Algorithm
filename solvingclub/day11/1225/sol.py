import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    tc = int(input())
    password_list = list(map(int, input().split()))

    def minus_def(lst):
        for i in range(1, 6):   # 1부터 5까지 빼주기
            x = lst.pop(0) - i  # 리스트 첫번째 요소를 리스트에서 빼서 i만큼 빼준 후
            lst.append(x)       # 리스트 뒤에 붙이기
            if lst[-1] <= 0:    # 만약 그 값이 0 이하가 되면 0으로 바꿔주고 for문 종료
                lst[-1] = 0
                break
        return lst

    result = True
    while result == True:
        minus_def(password_list)
        for n in range(len(password_list)): # 리스트를 순회하며 0보다 작은 값이 생길 때까지 while문 돌리기
            if password_list[n] <= 0:
                result = False

    print(f'#{tc}', end = " " )
    print(*password_list)


