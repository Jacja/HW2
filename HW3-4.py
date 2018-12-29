Определить, какое число в массиве встречается чаще всего.

#1

from collections import Counter

print(*Counter(input('Введите числа: ').split()).most_common()[0][0])


#2
numbers = [2, 4, -8, 38, 45, 4, 36, 4, 86]
i = 0
dictionary = {}
for i, number in enumerate(numbers):
    if numbers[i] in dictionary:
        dictionary[numbers[i]] += 1
    else:
        dictionary[numbers[i]] = 1
print(max(dictionary, key=dictionary.get))

#3
from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раза встречается -', num)
else:
    print('Все элементы уникальны')