T = int(input())
for test_case in range(1, T + 1):
    n, N = input().split()
    N = int(N)

    str_list = input().split()
    
    # 숫자로 바꾼 후 정렬. 정렬 후 다시 원래 문자열로 바꿔주기
    
    # 1. 숫자로 변환하기
    # number_list 요소의 인덱스 값이 바꿔줘야 되는 해당 숫자값임 ex) ONE의 인덱스 값 = 1 -> 숫자 1로 바꿔줘야 함
    number_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_list = []
    for i in range(len(str_list)):
        # count 변수 설정
        count = 0

        for j in range(len(number_list)):
            # str_list의 i번째 값과 number_list의 j번째 값이 다르면 계속 count에 1을 더해준다
            # count 값만큼이 해당 문자열의 숫자값이다.
            if str_list[i] != number_list[j]:
                count += 1
            else: # 값이 같을 경우 for문을 종료한다
                break
                
        new_list.append(count) # count 값을 new_list에 추가한다

    a = len(new_list)

    # 2. 숫자로 변환한 리스트를 정렬하기 (선택 정렬 사용)
    for i in range(a):
        # 최소값의 인덱스를 i로 설정
        min_idx = i
        # i의 다음부터 시작
        for j in range(i+1, a):
            # i의 값보다 j의 값이 작을 경우 min_idx를 j로 바꿔준다
            if new_list[i] > new_list[j]:
                min_idx = j
                new_list[i], new_list[j] = new_list[j], new_list[i] # i의 값과 j의 값의 자리를 바꿔주며 최소값이 앞으로 가게 정렬

    # 3. 정렬된 리스트를 다시 문자열로 변환하기
    # 변환한 문자열을 담을 빈 리스트 생성
    sort_list = []
    for x in range(len(new_list)):
        str_value = 0
        for y in range(len(number_list)):
            # 인덱스 x 일 때 new_list의 값이 number_list의 인덱스 값 y와 일치하면
            if new_list[x] == y:
                # str_value에  y일 때의 number_list 값(숫자)을 넣어준다
                str_value = number_list[y]
                break # 값을 찾았으니 for문 종료
        
        # 빈 리스트에 변환된 숫자 값(str_value)를 넣어준다
        sort_list.append(str_value)
        
    print(f'#{test_case}')
    print(*sort_list)