# Урок 2. Циклы (for, while)

# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input("Введите число монет на столе: "))
heads, tails = 0, 0
for i in range(n):
    x = int(input("Введите, орел(0) или решка(1)? - "))
    if x == 0:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)









