# 3 task
def myfunc():
    x = input('x=')
    resX = float((re.search(r'\d+', x)).group())
    if resX>=8:
        print(("F(x)=",-resX**2+resX-9))
        p = input("Продолжить тестирование программы? +/-")
        if p == "+":
            myfunc()
        else:
            return
    else:
        print("F(x)=",(1/(resX**4-6)))
        p = input("Продолжить тестирование программы? +/-")
        if p == "+":
            myfunc()
        else:
            return
myfunc()

