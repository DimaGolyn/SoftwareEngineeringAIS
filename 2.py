class Pelmeni:
    def __init__(self, name, brand, vkus, price):
        self.name = name
        self.brand = brand
        self.vkus = vkus
        self.price = price
    def WhatIsPelmeni(self):
        print(f"Это {self.name} да ещё и {self.brand}! О ДА!")

    def Info(self):
        print(f"А внутри у них {self.vkus}, а стоимость то {self.price} вообще супер, дайте 2 пачки!!!")

myPelmeni = Pelmeni("Пельмени", "Ревтенские", "свинина", "100 рублей")
myPelmeni.WhatIsPelmeni()
myPelmeni.Info()