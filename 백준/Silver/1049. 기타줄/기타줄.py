N, M = map(int, input().split())
min_v = 999999
min_pack = 999999
min_one = 999999

for _ in range(M):
    pack, one = map(int, input().split())
    if min_pack > pack:
        min_pack = pack
    if min_one > one:
        min_one = one

total = min(min_pack*((N // 6) + 1), min_pack * (N // 6) + min_one * (N % 6), min_one * N)

print(total)
