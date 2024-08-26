import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input()))
    # print(card_list)

    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt_list = [0] * 10 # 숫자 갯수를 저장할 빈 리스트

    for i in card_list: # 카드 리스트를 순회하며
        cnt_list[i] += 1    # 해당 숫자의 인덱스를 증가시켜 개수 저장
    # print(cnt_list)

    # cnt_list 를 순회하며 값이 제일 큰 인덱스 찾기
    # 제일 큰 인덱스가 가장 큰 숫자
    max_idx = 0   # 초기값 설정
    for n in range(len(cnt_list)):
        if cnt_list[max_idx] <= cnt_list[n]:    # n의 값이 max_idx 값보다 같거나 크면 증가(같으면 더 큰 숫자로 저장하기 위해)
            max_idx = n
    print(f'#{tc} {num_list[max_idx]} {cnt_list[max_idx]}')

    


