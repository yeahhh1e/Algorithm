import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))

    # print(num)
    
    count = [0] * 12 # 빈배열 만들기
    for i in range(6):
        count[num[0]%10] += 1 # 해당 숫자의 인덱스 자리에 더해주기
        num[0] = num[0] // 10 # 숫자를 몫만 남기기
    
    
    i = 0
    t = 0 # triplet 넣을 변수
    r = 0 # run 넣을 변수
    while i < 8:
        # triplet 검사
        if count[i] >= 3: # 3이상이면 트리플릿
            count[i] -= 3
            t += 1
            continue # 아래를 실행하지 않고 해당 인덱스 재검사
        
        # run 검사
        if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1: # 연속된 세자리가 1 이상이면 런
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            r += 1
            continue

        i += 1 # triplet, run 둘 다 해당되지 않으면 다음 인덱스 검사로 넘어감
    
    if t + r == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')



    
# # print(f'#{test_case} {result}')