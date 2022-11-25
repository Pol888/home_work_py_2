# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x1 = float(input()) + 100 # + 100, чтобы при * 10 не возникало погрешностей .. например: 0.56 * 10 = 5.6000000000000005
sum_number = 0
while x1 != 0:
    if x1 - int(x1) == 0:
        sum_number += x1 % 10
        x1 //= 10
    elif x1 - int(x1) != 0:
        x1 *= 10

print(int(sum_number) - 1)

# строковый вариант:
sum_number2 = 0
x2 = ''.join(input().split('.'))
for i in x2:
    sum_number2 += int(i)

print(sum_number2)


