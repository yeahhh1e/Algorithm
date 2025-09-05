import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    sentence = input.replace(' ', '')
    counter = Counter(sentence)
    most_common = counter.most_common()

    if
    max = -1
    most = '?'
    check = True

    for x in sentence:
        if x == ' ':
            continue
        cnt = 0

        if max < sentence[x]:
            max = sentence[x]

        if max < cnt:
            max = cnt
            most = x
            check = True

        elif max == cnt and most != x:
            check = False

    if check == True:
        print(most)
    elif check == False:
        print('?')


