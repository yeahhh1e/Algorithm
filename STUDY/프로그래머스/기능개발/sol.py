def solution(progresses, speeds):
    answer = []
    
    n = len(progresses) # n은 progresses와 speeds 배열의 길이이자 작업의 개수
    for i in range(n): # 0부터 끝까지 순회
        progress = progresses[i]
        speed = speeds[i]
        period = (100 - progress) // speed # 남은 개발 기간
        period_list = []
        period_list.append(period) # 개발 기간 리스트에 각각의 남은 개발 기간 추가
    
    return_list = [0]*101 # 개발기간이 아무리 길어도 100을 넘지 않으므로
    
    for i in range(len(period_list)): # 개발 기간 리스트 순회
        count = 0
        for j in range(i+1, len(period_list)):
            while period_list[i] > period_list[j]: # 리스트를 순회하며 i번째 기간보다 더 큰 기간이 나오기 전까지
                count += 1
        return_list[period_list[i]] = count # 개발 완료된 기능을 해당 날짜에 추가
        
    for m in return_list:
        if m > 0: # 0이 아니라면
            answer.append(m)
    
    return answer