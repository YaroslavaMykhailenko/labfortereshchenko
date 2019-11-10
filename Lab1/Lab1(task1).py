# 1 task
import re
i = 1
word = input("Enter your string:")
result = re.split(r'[B-Zb-z]', word)
if len(result)==1:
    for i in range(5):
        for i in range(8):
            print(result[0], end="")
        print()
else:
    print("Incorrect string")
