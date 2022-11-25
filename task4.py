# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
from random import randint
N = int(input())
list_elements = [randint(-N, N) for i in range(N)] # список из N элементов
fileTXT = [randint(0, N - 1) for i in range(randint(1, N - 1))] # рондомный список позиций
print(list_elements)
print(fileTXT)
composition = 1
for i in fileTXT:
    composition *= list_elements[i]

print(composition)
