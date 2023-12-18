# from pprint import pprint
#
# name_employee = ("Alice", "Bob", "Charlie")
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
#
# bonus = {name_employee[i]: salary[i] + salary[i] * (float(bonus[i][:-1]) / 100) for i in range(len(name_employee))}
#
# pprint(bonus)

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.

# INPUT
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
# OUTPUT
# {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}


def gen_dict(names: list[str], salary: list[int], bonus: list[str]):
    return {name: ((sal * int(bon.strip('%'))) / 100) for name, sal, bon in zip(names, salary, bonus)}


print(gen_dict([],[],[]))

#
# print(gen_dict(["Alice", "Bob", "Charlie"], [5000, 6000, 7000], ["10%", "5%", "15%"]))
# print(gen_dict(["Eva", "David", "Frank"], [7500, 8000, 9000], ["8%", "12%", "7%"]))
# print(gen_dict(["Grace", "John", "Linda"], [6200, 5800, 7500], ["9%", "3%", "12%"]))