import random
import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def arccos(n):
    return math.arccos(n)
operation = input("Введите нужный вам символ (+, -, *, /,  ^, mod, random, !, arccos): ")
if operation == "+":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    res = n1 + n2
    print("Результат: ", res)
elif operation == "-":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    res = n1 - n2
    print("Результат: ", res)
elif operation == "*":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    res = n1 * n2
    print("Результат: ", res)
elif operation == "/":
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    if n2 == 0:
        print('Делить на ноль нельзя')
    res = n1 / n2
    print("Результат: ", res)
elif operation == "^":
    n1 = float(input("Введите число: "))
    power = float(input("Введите степень: "))
    res = n1 ** power
    print("Результат: ", res)
elif operation == "mod":
    n1 = float(input("Введите число: "))
    mod = float(input("Введите делитель: "))
    res = n1 % mod
    print("Результат: ", res)
elif operation == "random":
    low = float(input("Введите нижнюю границу диапазона: "))
    high = float(input("Введите верхнюю границу диапазона: "))
    res = random.uniform(low, high)
    print("Результат: ", res)
elif operation == "!":
    n = int(input("Введите число для вычисления факториала: "))
    res = factorial(n)
    print("Результат: ", res)
elif operation == "arccos":
    n = float(input("Введите число для вычисления арккосинуса: "))
    res = arccos(n)
    print("Результат: ", res)
else:
    print("Неверный символ операции")