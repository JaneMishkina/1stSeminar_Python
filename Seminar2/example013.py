# Задача 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась 
# самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите 
# программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 Output: 2

# import random

# n_user = int(input("Введите количество дней:"))
# max_counter = 0
# counter = 0

# for i in range(n_user):
#     temp = (random.randint(-50,50))
#     print(temp, end=" ")
#     if temp > 0:
#         counter+=1
#         if counter > max_counter:
#             max_counter = counter
#     else:
#         counter = 0

# print(f"\nМаксимальный оттепель {max_counter} дня(ей)")

import random

n = int(input("Введите количество дней от 1 до 100: "))
count = 0
days = 0
maxDays = 0
while count < n:
    temp = random.randint(-50, 50)
    if temp > 0:
        days += 1

        if maxDays < days:
            maxDays = days

    else:
        days = 0
    print(temp, end=" ")
    count += 1
print(f"Максимальная оттепель = {maxDays}")