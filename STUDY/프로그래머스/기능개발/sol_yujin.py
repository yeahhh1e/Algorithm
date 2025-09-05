import math
progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    # 각 작업이 완료되기까지 남은 일수를 계산하여 리스트에 저장
    left_days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]

    cur_day = left_days[0]  # 현재 배포 기준이 되는 날
    head = 0  # 처리 중인 작업의 시작 인덱스
    answer = []  # 결과를 저장할 리스트

    while head < len(left_days):  # 모든 작업을 처리할 때까지 반복
        temp = 0  # 이번 배포에서 완료될 작업 수를 저장

        for i in range(head, len(left_days)):  # 현재 인덱스부터 작업 확인
            if cur_day < left_days[i]:  # 다음 작업이 현재 기준일보다 더 오래 걸릴 경우
                cur_day = left_days[i]  # 배포 기준일을 갱신
                break  # 현재 배포 종료

            temp += 1  # 배포 가능한 작업 수 증가
            head += 1  # 처리한 작업 인덱스 이동

        if temp > 0:  # 배포 가능한 작업이 있다면
            answer.append(temp)  # 결과 리스트에 추가

    return answer  # 결과 반환
print(solution(progresses, speeds))