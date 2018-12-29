В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

#1
from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index, ':', arr[index])


#2
numbers = [3, -5, 6, 2, 46, 86, 6, -3, 4, -600, 2, 2, 2, 5, 34, 6, 5, 4, -3, -600, -1145]
max = -1
for i, number in enumerate(numbers):
    if number < 0 and (max < 0 or abs(number) < abs(numbers[max])):
        max = i
print(max, numbers[max])