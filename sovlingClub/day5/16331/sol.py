import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = []
    for _ in range(0,2):
        str = input()
        str_list.append(str)
    
    str1 = str_list[0]
    str2 = str_list[1]
    
    n = len(str1)
    m = len(str2)
   
    # 탐색할 문자열의 길이에서 찾는 문자열의 길이를 뺀 수 + 1 만큼이 총 탐색횟수
    r = m - n + 1
    # 0부터 r까지 탐색해줌
    for i in range(0, r+1):
        if str1 == str2[i:i+n]: # str2에서 i부터 i+n의 문자길이-1까지 자른 문자열이랑 비교
            result = 1
            break
        else:
            result = 0
    print(f'#{test_case} {result}')