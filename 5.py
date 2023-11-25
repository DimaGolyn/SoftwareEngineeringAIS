class Pelmeni:
    def __init__(self, name, brand, vkus, price):
        self.name = name
        self.brand = brand
        self.vkus = vkus
        self.price = price

    def Vkus(self):
        pass
class OldPelmeni(Pelmeni):
    def __init__(self, name, brand, vkus, price, razmer):
        super().__init__(name, brand, vkus, price)
        self.razmer = razmer
    def Vkus(self):
        print(f"{self.brand}! их {self.vkus} станет не такой вкусной чрезе недели 3, а про их стоимость можно и не говорить.")
class NewPelmeni(Pelmeni):
    def __init__(self, name, brand, vkus, price):
        super().__init__(name, brand, vkus, price)
    def Vkus(self):
        print(f"{self.brand}! их {self.vkus} станет не очень через 2 недели, а стоимость примерно {self.price}")

myPelmeni = NewPelmeni("Пельмени", "Бульмени", "Бульон", "125")
myOldPelmeni = OldPelmeni("Пельмени","Уральские", "курица", "69", "маленькие")

myPelmeni.Vkus()
myOldPelmeni.Vkus()
