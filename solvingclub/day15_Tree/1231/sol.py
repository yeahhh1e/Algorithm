import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    node_list = [list((input().split())) for _ in range(N)]
    # print(node_list)
    
    # parent = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    str_list = [0] * (N+1)
    for i in node_list:
        for j in range(len(i)):
            if j == 0: # 첫 번째는 부모 정점
                str_list[int(i[j])] = i[1] # 부모 정점 값을 2번째 값으로 설정
            elif i[j].isdigit() == True: # 문자열이 아닌 숫자라면 자식 정점이라는 뜻이므로
                if left[int(i[0])] == 0:  # 왼쪽 자식이 없으면 왼쪽 자식에 추가
                    left[int(i[0])] = i[j]
                else:   # 왼쪽이 있으면 오른쪽 자식 추가
                    right[int(i[0])] = i[j]
    print(f"#{tc}")
    # for n in range(N+1):
    def find_left():


        for m in range(N, 0, -1): # 거꾸로 순회하며 0이 아닌 수가 있는 인덱스 뽑기
            if left[m] != 0:
                print(str_list[int(left[m])]) # 왼쪽 뽑기
                left[m] = 0 # 0으로 바꿔주기
                print(str_list[m]) # 본인 뽑기
                if right[m] != 0:   # 오른쪽 있으면 뽑기
                    print(right[m])
                k = str(m)
                if k in left: # 왼쪽 자식이면
                    x = left.index(k)
                    print(str_list[x])  # 본인 뽑기
                    print(str_list[int(right[x])]) # 오른쪽 뽑기
                else:   # 오른쪽 자식이면
                    x = right.index(k)
                    print(str_list[x])  # 본인 뽑기
                    print(str_list[int(right[x])])  # 오른쪽 뽑기
                y = str(x)
                if y in left:
                    m = left.index(y)
                    print(str_list[m])
                    print(str_list[int(right[m])])

    # print(right)
    # print(left)
    # print(str_list)