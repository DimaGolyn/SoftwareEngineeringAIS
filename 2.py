import random
def Dice():
    x = random.randint(1, 6)
    print(x)
    if x == 5 or x == 6:
        print('Вы победили!')
    elif x == 3 or x == 4:
        Dice()
    elif x == 1 or x == 2:
        print('Вы проиграли!')
    else:
        print('Введены неверные числа')

if __name__ == '__main__':
    Dice()
