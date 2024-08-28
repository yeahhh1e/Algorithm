import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    node_list = [list((input().split())) for _ in range(N)]
    
    left = [0] * (N+1)
    right = [0] * (N+1)
    str_list = [0] * (N+1)

    # left, right, str_list 만들기
    for i in node_list:
        for j in range(len(i)):
            if j == 0: # 첫 번째는 부모 정점
                str_list[int(i[j])] = i[1] # 부모 정점 값을 2번째 값으로 설정
            elif i[j].isdigit() == True: # 문자열이 아닌 숫자라면 자식 정점이라는 뜻이므로
                if left[int(i[0])] == 0:  # 왼쪽 자식이 없으면 왼쪽 자식에 추가
                    left[int(i[0])] = i[j]
                else:   # 왼쪽이 있으면 오른쪽 자식 추가
                    right[int(i[0])] = i[j]

    print_value = []  # 출력할 값 담는 리스트
    def find_node(x):
        # 1. 자식 찾기
        # 왼쪽 자식이 있는지 탐색
        if left[x] != 0:
            find_node(int(left[x])) # 있으면 자식 계속 탐색
            return str_list[x]
        # 왼쪽 없으면 오른쪽 탐색
        elif right[x] != 0:
            if str_list[x] != 0:
                print_value.append(str_list[x])
            str_list[x] = 0 # 다시 탐색 방지 위해 0으로 바꿔줌
            find_node(int(right[x]))    # 얘도 자식이 있는지 확인
        else: # 2. 자식이 없다면 부모 탐색
            if str(x) in left: # x를 왼쪽 자식으로 갖고 있으면
                q = left.index(str(x))  # 부모 노드 값 q를 설정
                if q != 0:
                    if str_list[x] != 0:   # 위로 올라가기 전에 출력
                        print_value.append(str_list[x])
                    str_list[x] = 0
                    left[q] = 0
                    find_node(q)    # q의 다른 자식 있는지 찾기
            elif str(x) in right:   # x를 오른쪽 자식으로 갖고 있으면
                q = right.index(str(x))
                if q != 0:
                    if str_list[x] != 0:
                        print_value.append(str_list[x])
                    str_list[x] = 0
                    right[q] = 0
                    find_node(q)

    find_node(1)
    result = "".join(print_value)
    print(f"#{tc} {result}")