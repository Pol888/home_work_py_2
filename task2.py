# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input())
a_set_of_works = [1]
if N > 0:
    for i in range(2, N + 1):
        a_set_of_works.append(a_set_of_works[-1] * i)
elif N < 0:
    for i in range(0, N - 1, -1):
        a_set_of_works.append(a_set_of_works[-1] * i)

print(a_set_of_works)