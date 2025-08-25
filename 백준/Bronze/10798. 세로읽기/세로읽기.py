arr = [list(map(str, input())) for _ in range(5)]

max_len = max(map(len, arr))
result = []
for i in range(max_len):
    for j in range(len(arr)):
        try:
            result.append(arr[j][i])
        except IndexError:
            continue
print(''.join(result))