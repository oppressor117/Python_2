from typing import Union


class InvalidTextError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidNumberError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None
    _text = ''
    _number = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if text == "":
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
        elif not isinstance(text, str):
            raise InvalidTextError(f"Высота должна быть положительной, а не {text}")

        self._text = text

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")

        self._number = number


invalid_archive_instance = Archive("Sample text", -5)
print(invalid_archive_instance)

