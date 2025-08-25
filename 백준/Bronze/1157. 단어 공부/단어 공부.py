word = input().upper()
di = {}
for i in word:
    di[i] = 0

for j in word:
    di[j] += 1

max_value = max(di.values()) # 3

result = [k for k,v in di.items() if max(di.values()) == v]
if len(result) >= 2:
    print('?')
else:
    print(*result)