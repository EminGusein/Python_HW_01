# Урок 2. Циклы (for, while)

# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input("Введите число: "))
# x = 0
# k = 0
# while x <= n:
#     x = 2 ** k
#     if x <= n:
#         print(x, end=' ')
#     k += 1
for k in range(n):
    x = 2 ** k
    if x <= n:
        print(x, end=' ')

