# 2. В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

# Ввод:
# текст отсюда(https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81)

import webbrowser
import string

web = webbrowser.open("https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81")

data = input()

for char in string.punctuation:
    data = data.lower().replace(char, ' ')

counter_dict = {}

for word in data.split():
    counter_dict[word] = counter_dict.get(word, 0) + 1

counter_dict = tuple(sorted(counter_dict.items(), key=lambda item: item[1]))
for index, word in enumerate(counter_dict[-1:-11:-1], 1):
    print(f'{index}. {word[0]:>20} {word[1]} раз')

