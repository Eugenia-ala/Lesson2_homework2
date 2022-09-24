# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Решение 1
# print("Insert number: ")
# number = int(input())
# sum = 0
# while number !=0:
#     p = number % 10
#     sum = sum + p # или sum += p
#     number = number // 10
# print(sum)

# # Решение 2
# number = input("Insert number: ")
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# print("Insert number: ")
# N = int(input())
# fact = 1
# list = []
# for i in range(1, N + 1):
#     list.append(fact * i)
#     fact *= i
# print(list)

# Задайте список из n чисел последовательности (1 + 1 / n) в степени n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# print("Insert number: ")
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += (1 + 1 / i) ** i
# print(sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import
# n = int(input())
# list = [randit(-n, n) for _ in range(randint(5, 10))]
# print(list)
#
# f = open("newtext.txt", "w")
# for i in range(randint(2, len(list)));
#     f.write(str(randint(0, len(list) - 1)) + "\n")
# f.close()
#
# pr = 1
# with open("newtext.txt", "r") as f:
#     for i in f.read(),splitlines():
#         pr = pr * list[int(i)]
# print(pr)


# Реализуйте алгоритм перемешивания списка.

# import random
# n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(n)
# print(n)

