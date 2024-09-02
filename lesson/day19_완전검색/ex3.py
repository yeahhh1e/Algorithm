def KFC(x):
    KFC(x + 1) # 정지 조건이 없어서 python은 재귀 깊이 제한 1,000

KFC(0)
print('끝')