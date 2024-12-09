# import sys
# sys.stdin = open('input.txt')

food = [1, 3, 4, 6]

water = 0 # 물
N = len(food)-1 # 음식의 종류 수
food_list = [] # 음식을 배열할 리스트

for i in range(1, N+1):
    i_food = food[i] // 2 # i번째 음식을 2로 나눔
    if i_food >= 1: # 2개 이상이 존재한다면 배열함
        for n in range(1, i_food+1): # 몫만큼 배열하기
            food_list.append(i) 
    else: # 음식이 2개 미만으로 존재하므로 배열하지 않음
        continue

# 순회가 끝나면
reverse_food_list = list(reversed(food_list))
answer_list = []
water = [0]
answer_list = food_list + water + reverse_food_list
answer = ''.join(str(s) for s in answer_list)


print(answer)
# answer = ''
# answer
# M = len(food_list) # 한 선수가 먹을 음식 수
# answer = food_list
# answer.append(water) # 배열의 마지막에 물 넣어주기
#
#
#
#
# print(answer)