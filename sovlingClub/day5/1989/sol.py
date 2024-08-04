import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()

    # 빈 문자열 만들기
    reverse_str = ""
    for j in string:
        # 거꾸로 저장
        reverse_str = j + reverse_str
    
    if reverse_str == string:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')