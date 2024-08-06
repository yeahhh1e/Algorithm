import sys
sys.stdin = open("input.txt", "r")

# 이진탐색 함수
# 시작페이지: l , 마지막페이지: r, 찾을 페이지 : k
def find_num(l, r, k):
    c = int((l + r)//2)
    cnt = 0 # 탐색 횟수 변수 설정
    while True:
        if c < k: # 찾을 페이지보다 중간 페이지가 작으면 c 기준 오른쪽 구간 탐색
            l = c # 시작점이 찾은 중간페이지 c가 됨
            c = int((l + r)//2) # c를 새로 구함
            cnt += 1
        elif c > k:  # 찾을 페이지보다 중간 페이지가 크면 c 기준 왼쪽 구간 탐색
            r = c # 마지막 페이지가 중간 페이지가 됨
            c = int((l + r)//2)
            cnt += 1
        else: # c == k 찾으면 종료
            break
    return cnt 
   
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pages = list(map(int, input().split()))

    r = pages[0]
    k1 = pages[1] # A가 찾을 페이지
    k2 = pages[2] # B가 찾을 페이지

    result_a = find_num(1, r, k1)
    result_b = find_num(1, r, k2)
    
    # 탐색횟수 cnt가 작은 사람이 이김
    if result_a < result_b: # A가 이김
        result = "A"
    elif result_a > result_b: # B가 이김
        result = "B"
    else: # 둘이 같은 횟수로 비김
        result = 0

    print(f'#{test_case} {result}')