F = input("Напишите предложение на английском: ").lower()
a = 0
for letter in F:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        a+=1
NewF = F.replace("ugly", "beauty")
print(f"Длина предложения = {len(F)} символов. \nКоличество искомых гласных = {a}. \nНовая фраза = {NewF}."
      f"\n Начинается ли предложение с The - {NewF.startswith('The')}. \nЗаканчивается ли на end - {NewF.endswith('end')}")