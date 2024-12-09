def solution(food):
    water = food[0] # 물
    N = len(food)-1 # 음식의 종류 수
    food_list = [] # 음식을 배열할 리스트

    for i in N:
        i_food = food[i] // 2 # i번째 음식을 2로 나눔
        if i_food >= 1: # 2개 이상이 존재한다면 배열함
            for n in i_food: # 몫만큼 배열하기
                food_list.append(i) 
        else: # 음식이 2개 미만으로 존재하므로 배열하지 않음
            continue

    # 순회가 끝나면
    M = len(food_list) # 한 선수가 먹을 음식 수
    answer = food_list
    food_list.append(water) # 배열의 마지막에 물 넣어주기
    for n in food_list[:-2:-1]: # 처음부터 물 제외하고 마지막까지 거꾸로 넣어주기
        answer.append(n)
    


    return answer