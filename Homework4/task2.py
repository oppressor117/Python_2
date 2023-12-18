# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def kwargs_to_dict(**kwargs):
    return {value if isinstance(value, int | str | float | bool | tuple) else str(value): key for key, value in
            kwargs.items()}


print(kwargs_to_dict(rev=True, acc="YES", stroka=4))