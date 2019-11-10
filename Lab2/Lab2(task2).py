# Task2
print("Михайленко Ярослава Євгенівна \nЛабораторна робота №2 \nВаріант 10 \nВиведення чисел \n")
import re
def whole_func():
    granica = input("Верхню границю: ")
    chislo_m =input("Уведіть значення квадрату: ")
    result_granica = int((re.search(r'\d+', granica)).group())
    result_chislo = int((re.search(r'\d+', chislo_m)).group())
    final_number = 'Числа, которые пододходят под условие:'
    for iter in range(result_granica):
        sum_number = 0
        for new_number_value in str(iter):
            sum_number = sum_number + int(new_number_value)
        if sum_number ** 2 == result_chislo:
            final_number = final_number + ' ' + str(iter)
    print(final_number)
    c = input("Продолжить тестирование программы? +/-")
    if c == '+':
        whole_func()
    else:
        return ()


whole_func()
