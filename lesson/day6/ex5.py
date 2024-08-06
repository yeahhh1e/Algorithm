# 고지식한 검사
target = "Hello SSAFY 12th!" # target 패턴을 찾을 대상
pattern = "SSA" # 우리가 찾을 패턴

def BruteForce(pat, text):
    N = len(text) # 타겟의 길이
    M = len(pat) # 패턴의 길이
    i = 0 # text의 인덱스
    j = 0 # 패턴의 인덱스

    while j < M and i < N:  # 길이보다 인덱스가 작을 때

        # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
        if text[i] != pat[j]:
            # text의 현재 위치에서 일치하지 않는 곳을 발견 !
            # 지금위치 - j + 1
            i = i - j

            j = -1
        i += 1
        j += 1

        # 검색 성공
        if j == M:
            return i - M
        else:
            return -1

# 심플 버전
text = "This is simple version"
pattern = 'si'
def BruteForceV2(pat, text):
    for idx in range(len(text) - len(pat) + 1):
        # 패턴을 처음부터 끝까지 순회

        #1. 다르면, break
        if text[idx + j] != pat[j]:
            break
        # 같다면(다른 게 없다면)
        else:
            return idx
    else:
        return -1

