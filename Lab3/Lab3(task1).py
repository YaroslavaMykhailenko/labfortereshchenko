# Task 1
import string
import re

def CapsToString(result,big_string):
    val = " "   # Тут будет Новая строка(переделан. result)
    number_count =0
    for i in result:
        if len(i) > number_str:
            my_str = i.split(' ')
            my_str2 = ''
            for y in my_str:
                word_upper = re.sub(r'[a-z]([A-Z])', r'-\1', y[big_string]).upper()
                my_str2 +=' '+ y.replace(y[big_string], word_upper)
            print(my_str2)
           # val += " " + string.capwords(i)
            number_count +=1
    return ''

s1 = input("Введіть речення: ")
big_string = int(input("Введите номер буквы(каждого слова),которую хотите сделать большой: "))
number_str = int(input("Введіть довжину слова: "))
result = re.split(r'\d', s1)
print(CapsToString(result,big_string))
