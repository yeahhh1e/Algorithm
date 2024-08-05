t = 'TTA'
p = 'TTTTTATTAATA'

N = len(t)  # 3
M = len(p)  # 8
cnt = 0

for i in range(N-M+1):  # 비교 시작 위치
    for j in range(M):
        if t[i + j] != p[j]: # 불일치시 브레이크
            break            # for j에 대한 break, 다음 j부터 비교 시작
    else:                    # for j가 중단없이 반복되면
        cnt += 1             # 패턴 개수 1 증가
print(cnt)