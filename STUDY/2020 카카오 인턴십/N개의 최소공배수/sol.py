def solution(arr):
    answer = 1
    
    common_divisor = []
    N = len(arr)

    for i in range(2, max(arr)+1): # 2부터 약수 찾기
        new_arr = [0]*N
        check = False # 약수 추가 확인 변수
        more = True # 한 번 더 순회할지 결정하는 변수
        divisor = []
        while more == True:
            count = 0
            for j in range(N): # 배열의 요소를 순회하면서
                if arr[j] % i == 0: # 나머지가 0이라면(== i가 약수라면)
                    count += 1
                    new_arr[j] = arr[j] // i # 몫으로 바꿔주기
                    if check == False: # 추가 전이라면
                        divisor.append(i) # 약수리스트에 추가
                        check = True
                else: # 약수가 아니라면
                    new_arr[j] = arr[j] # 그대로 수 추가
            if count >= 2:  # 2개 이상의 수에게 약수라면(모두 서로소가 아닌 상태)
                arr = new_arr[:] # new_arr로 바꿔주기
                common_divisor += divisor  # 공약수 리스트와 약수 리스트 합치기
            else:
                more = False


    for n in arr:
        answer *= n
    if common_divisor: # 공약수 리스트가 있다면
        for m in common_divisor:
            answer *= m

    return answer
# print(solution([3,9,14,18,21,22,27,30]))