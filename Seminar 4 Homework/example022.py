# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те 
# числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит 
# сами 
# элементы множеств.

from random import randint

a = int(input("Введите количество чисел для 1-го набора: "))
b = int(input("Введите количество чисел для 2-го набора: "))
list_a = [randint(1, 19) for i in range(a)]
list_b = [randint(1, 19) for i in range(b)]
print(f"{list_a}\n{list_b}")

list_a = set(list_a)
list_b = set(list_b)
print(f"{list_a}\n{list_b}")

result = list_a.intersection(list_b)
print(result)

result = list(list_a.intersection(list_b))
print(result)

result.sort()
print(result)

# from random import randint as RD
# n = int(input("Введите количество элементов 1 массива : "))
# a = [RD(0,100) for _ in range(n)]
# n = int(input("Введите количество элементов 2 массива : "))
# b = [RD(0,100) for _ in range(n)]
# print("Массив состоит из: ", *a)
# print("Массив состоит из: ", *b)
# mult_rez = set(a) & set(b)
# print("Упорядоченное множество целых чисел сгенерированных массивов: ", sorted(mult_rez))
