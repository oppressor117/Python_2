#
# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))
num = number
h = hex(num)
hex_strings = "0123456789abcdef"
hex_number = ""

while number > 0:
    remainder = number % 16
    hex_string = hex_strings[remainder]
    hex_number = hex_string + hex_number
    number //= 16

if hex_number == h[2:]:
    print(f'{hex_number = }\n{h = }\n{True}')
else:
    print(f'{hex_number = }\n{h = }\n{False}')












