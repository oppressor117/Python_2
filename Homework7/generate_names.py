# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.


from random import randint
VOWELS = "EYUIOA"


def rnd_name():
    name_len = randint(4,7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))    # перегоняем числа с помощью чар в букву, 65-90 это англ алфавит
        for i in name:
            if i in VOWELS:
                return name.capitalize()




