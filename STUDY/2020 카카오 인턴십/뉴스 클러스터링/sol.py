

# 두글자씩 끊는 함수
def split_char(string, lst):
    for i in range(len(string)-1):
        if string[i].isalnum() == False:
            pass
        elif string[i+1].isalnum() == False:
            pass
        else:
            lst.append(string[i:i + 2].upper()) # 대문자로 바꿔주기
    print(lst)
    upper_lst = []
    # for i in lst:
    #     upper_lst.append(i.upper())
    # return upper_lst
new_char = []    
# print(split_char('FRENCH', new_char))

# 자카드 유사도 구하기
def jaccard(str1, str2):
    s1 = []
    s2 = []
    split_char(str1, s1)
    split_char(str2, s2)
    print(s1, s2)
    # inter_list = set(s1) & set(s2)
    # union_list = set(s1) | set(s2)
    inter_list = []
    union_list = []
    print(inter_list, union_list)
    
    if len(inter_list) == 0 and len(union_list) == 0:
        jaccard = 1
    else:
        jaccard = int((len(inter_list) / len(union_list))*65536)
    return jaccard

# 합집합 구하는 함수
def union_lst(s1, s2):
    global inter_list
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                inter_list.append(s1[i])
    s[i] 

def solution(str1, str2):
    answer = jaccard(str1, str2)
    return answer
