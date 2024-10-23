def solution(expressions):
    answer = []
    

    N = len(expressions)
    list(expressions)

    # 표현식에서 제일 큰 숫자 찾기
    max_v = 0
    for i in range(N):
        split_list = list(expressions[i].split())
        for n in split_list:
            for m in n:
                if m.isdigit() == True:
                    m = int(m)
                    if max_v < m:
                        max_v = m

    for x in range(max_v+1, 10):
        for y in range(N):
            split_list = list(expressions[i].split())
            A = split_list[0]
            B = split_list[1]
            C = split_list[2]


            for x in list(A)
                    A = m *(max_v+1)
                    B =
    return answer
def find_base(num, value):
    list(num)
    for i in list()
solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]	)