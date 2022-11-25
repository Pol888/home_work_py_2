#Реализуйте алгоритм перемешивания списка.
from random import randint

n = int(input())
list_elements = [i for i in range(n)]
print(list_elements)

for i in range(len(list_elements)):
    x = randint(0, len(list_elements) - 1)
    list_elements[i] , list_elements[x] = list_elements[x], list_elements[i]
print(list_elements)