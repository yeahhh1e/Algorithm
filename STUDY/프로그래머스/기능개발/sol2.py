import math

progresses = [95, 95, 95, 95]
speeds = [4, 3, 2, 1]
print(progresses, speeds)
answer = []

n = len(progresses)
period_list = []
# n은 progresses와 speeds 배열의 길이이자 작업의 개수
for i in range(n): # 0부터 끝까지 순회
    progress = progresses[i]
    speed = speeds[i]
    period = math.ceil((100 - progress) / speed) # 남은 개발 기간

    period_list.append(period) # 개발 기간 리스트에 각각의 남은 개발 기간 추가

return_list = [0]*101 # 개발기간이 아무리 길어도 100을 넘지 않으므로

for i in range(len(period_list)): #개발 기간 리스트 순회
    if period_list[i] == 999:
        pass
    else:
        day = period_list[i] # 몇번째 날인지 저장
        count = 1
        for j in range(i+1, len(period_list)):

            if period_list[i] >= period_list[j]: # 리스트를 순회하며 i번째 기간보다 더 큰 기간이 나오기 전까지
                count += 1
                if j == len(period_list)-1:
                    period_list[i:j+1] = [999] * (j+1 - i)
            else:
                period_list[i:j] = [999]  * (j - i)
                break

        return_list[day] = count # 개발 완료된 기능을 해당 날짜에 추가

for m in return_list:
    if m > 0: # 0이 아니라면
        answer.append(m)

print(answer)