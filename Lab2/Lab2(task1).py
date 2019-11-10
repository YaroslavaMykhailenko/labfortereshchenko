# Task 1
print("Михайленко Ярослава Євгенівна \nЛабораторна робота №2 \nВаріант 10 \nВиведення чисел \n")
import re
def func():
    upper_border =input("Введіть значення верхньої межі n(≥1):")
    result_upper =int((re.search(r'\d', upper_border)).group())
    if  result_upper<1:
        print("n має бути ≥ 1")
        func()


    argument =input("Введіть значення аргумента функції:")
    result_argument =int((re.search(r'\d', argument)).group())
    if result_argument == 0:
        print("Введіть ненулевий аргумент функції!")
        argument =input("Введіть значення аргумента функції:")

    multiplication = 1
    for down_border in range(result_upper):
        down_border = down_border + 1

    multiplication = multiplication * (result_argument+down_border)/(down_border ** 2)

    print(multiplication)


    c = input("Продовжити тестування програми? +/-")
    if c == "+":
        func()
    else:
        return()

func()
