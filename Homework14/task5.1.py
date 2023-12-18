
import os
import sys
import pytest

# Текущее имя файла
current_filename = __file__

# Новое имя файла с добавлением "test_" в начале
new_filename = "test_1.py"
                #+ os.path.basename(current_filename))

# Откройте текущий файл для чтения
with open(current_filename, 'r') as source_file:
    source_code = source_file.read()
    source_file.close()

# Запишите код в новый файл
with open(new_filename, 'w') as new_file:
    new_file.write(source_code)
    new_file.close()

with open(new_filename, 'r') as new_file:
    file_contents = new_file.read()
    # Выводим содержимое файла на экран
    #print(file_contents)



# Открываем файл для записи
with open('pytest_output.txt', 'w') as file:
    # Перенаправляем stdout в файл
    sys.stdout = file

    # Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])

# Возвращаем stdout в исходное состояние
sys.stdout = sys.__stdout__
# Считываем содержимое файла
with open('pytest_output.txt', 'r') as file:
    lines = file.readlines()
    first_line = file.readline()
    first_five_lines = lines[:1]

# Выводим первые 5 строк
for line in first_five_lines:
    print(line)

