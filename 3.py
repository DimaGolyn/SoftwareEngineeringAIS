a = int(input("Введите число от 0 до 10: "))
if a>10 or a<0:
    print("Числе не в диапазоне.")
elif (a >= 0 and a < 4):
    print("От 0 до 3 включительно")
elif (a >= 4 and a < 6):
    print("От 3 до 6")
elif (a >= 6 and a < 11):
    print("От 6 до 10 включительно")