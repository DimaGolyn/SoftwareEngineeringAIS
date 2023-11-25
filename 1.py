class Pelmeni:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def WhatIsPelmeni(self):
        print(f"Это {self.name} да ещё и {self.brand}! О ДА!")

myPelmeni = Pelmeni("Пельмени", "Ревтенские")
myPelmeni.WhatIsPelmeni()