import math
def solution(progresses, speeds):
    answer = []

    n = len(progresses) # n은 progresses와 speeds 배열의 길이이자 작업의 개수
    period_list = []

    for i in range(n): # 0부터 끝까지 순회
        progress = progresses[i]
        speed = speeds[i]
        period = math.ceil((100 - progress) / speed) # 남은 개발 기간

        period_list.append(period) # 개발 기간 리스트에 각각의 남은 개발 기간 추가

    return_list = [0]*101 # 개발기간이 아무리 길어도 100을 넘지 않으므로

    for i in range(len(period_list)): # 개발 기간 리스트 순회
        if period_list[i] == 999:
            pass
        else:
            day = period_list[i] # 몇번째 날인지 저장
            count = 1 # 개발한 기능의 수를 저장할 변수
            for j in range(i+1, len(period_list)): # i번째 다음부터 순회

                if period_list[i] >= period_list[j]: # 리스트를 순회하며 i번째 기간보다 더 큰 기간이 나오기 전까지 기능 수 +1
                    count += 1
                    if j == len(period_list)-1: # 마지막 인덱스까지 순회했다면 탐색이 끝났으므로 999로 바꿔주기
                        period_list[i:j+1] = [999] * (j+1 - i)
                else:
                    period_list[i:j] = [999]  * (j - i) # count에 추가한 기능은 999로 바꿔 탐색에서 제외시키기
                    break

            answer.append(count) # 개발 완료된 기능을 해당 날짜에 추가

    return answer