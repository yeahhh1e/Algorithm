def solution(food):
    N = len(food) - 1  # 음식의 종류 수
    food_list = []  # 음식을 배열할 리스트

    for i in range(1, N + 1):
        i_food = food[i] // 2  # i번째 음식을 2로 나눔
        for n in range(1, i_food + 1):  # 몫만큼 배열하기
            food_list.append(i)

    reverse_food_list = list(reversed(food_list))  # 음식 리스트를 거꾸로 뒤집어줌
    water = [0]  # 물
    answer_list = food_list + water + reverse_food_list
    answer = ''.join(str(s) for s in answer_list)

    return answer
