# task 2
import re
def myfunc():
    resA = int(re.match(r'\d+', input("Введіть число а:")).group())
    resB = int(re.match(r'\d+', input("Введіть число b:")).group())
    resC = int(re.match(r'\d+', input("Введіть число c:")).group())
    resK = int(re.match(r'\d+', input("Введіть число k:")).group())
    if resA % resK == 0:
        print("Число k є дільником числа a")
    elif resB % resK == 0:
        print("Число k є дільником числа b")
    elif resC % resK == 0:
        print("Число k є дільником числа c")
    else:
        print("Число k не є дільником жодного з чисел")

    p = input("Продолжить тестирование программы? +/-")
    if p == "+":
        myfunc()
    else:
        return
myfunc()