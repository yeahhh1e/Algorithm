answer = 0
n = 2
# 1. 2진수 변환
bin_n = bin(n) # 0bxxxx형식
print(bin_n)
next_n = 0
# 2. 1의 갯수 세기
real_n = bin_n[2:] # 0b 제거
print(real_n)
count = 0
for i in real_n:
    if i == '1':
        count += 1

list_n = list(real_n) # 리스트 형식으로 변환
# 3. n보다 큰 자연수 찾기
if len(real_n) == count:  # n이 전부 1로 구성되어 있다면, 다음으로 큰 수는 두번째가 0이고 나머지를 1로 채우기
    m = '1' * (count+1)
    list_m = list(m)
    print(m[1])
    list_m[1] = '0'
    list_n = list_m
    # real_m = "".join(list_m)
    # print(real_m)
    # answer = int(real_m, 2)

# 전부 1이 아니라면, 다음 큰 수 찾기
elif len(real_n) == count + 1: # 0이 하나고 나머지가 다 1이라면 0을 1로 바꾸기
    for i in list_n:
        if i == '0':
            i = '1'


else: # 뒤에서부터 '01' 찾아서 '10'으로 바꾸기
    for i in range(len(list_n) -1, 0, -1):
        x = 0
        if list_n[i-1] == '0' and list_n[i] == '1':
            list_n[i - 1], list_n[i]  = '1', '0'
            x = i
            # 뒤에 부분 남은 1의 갯수만큼 뒤에 채우고 앞은 0으로 채우기
            new_list = list_n[i:]
            ones = new_list.count('1')
            # print(ones)
            for j in range(len(new_list)-1, 0, -1):
                if ones == 0:
                    for y in range(0, j+1):
                        new_list[y] = '0'
                    break
                else:
                    new_list[j] = '1'
                    ones -= 1
            list_n = list_n[0:i] + new_list
            break



answer = int("".join(list_n), 2)
print(answer)
