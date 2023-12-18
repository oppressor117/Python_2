"""
Напишите функцию группового переименования файлов.
Она должна:
принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла.

Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os


def rename_files(
    directory,
    new_filename,
    num_digits=2,
    source_extension=None,
    dest_extension=None,
    name_range=None,
):
    # Получаем список файлов в исходной директории
    files = os.listdir(directory)

    # Проходим по списку и переименовываем только файлы с указанным расширением
    for i, filename in enumerate(files, start=1):
        # Игнорируем файлы без указанного расширения (если параметр source_extension задан)
        if source_extension and not filename.endswith(source_extension):
            continue

        # Получаем расширение файла
        file_name, file_extension = os.path.splitext(filename)

        # Определяем диапазон символов для сохранения из имени файла
        if name_range:
            start, end = name_range
            original_name_part = file_name[start - 1 : end]  # noqa
        else:
            original_name_part = file_name

        # Генерируем порядковый номер
        format_string = "{:0" + str(num_digits) + "d}"
        order_number = format_string.format(i)

        # Генерируем новое имя файла
        new_name = (
            f"{original_name_part}_{new_filename}_{order_number}{dest_extension or file_extension}"
        )

        # Полный путь к старому и новому файлам
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(old_path, new_path)

        print(f"Переименован файл {filename} в {new_name}")



directory = r"C:\Users\Оля\OneDrive\Рабочий стол\Учеба\Python\.Homeworks\Homework7"  # Путь к исходной директории
new_filename = "new_name"  # Желаемое конечное имя файла (может быть None)
num_digits = 3  # Задайте желаемое количество цифр в порядковом номере
source_extension = ".txt"  # Расширение исходных файлов (может быть None)
target_extension = ".jpg"  # Расширение конечных файлов (может быть None)
name_range = [3, 6]  # Диапазон для оригинального имени файла (может быть None)
rename_files(
    directory, new_filename, num_digits, source_extension, target_extension, name_range
)