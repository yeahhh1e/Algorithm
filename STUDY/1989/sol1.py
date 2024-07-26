import sys

sys.stdin = open('input.txt')

# 입력
T = int(input())
lst = []
for _ in range(T): # T 수만큼 단어 입력 받기
    N = input()
    lst.append(N) # N을 빈 리스트 lst에 추가

# 처리
for i, string in enumerate(lst, start=1): # 인덱스 1부터 시작
    reversed_string = string[::-1] # 문자열 거꾸로 배열
    if reversed_string == string: # 원래 문자열과 비교
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')



  
