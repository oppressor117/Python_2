# Введите ваше решение ниже
import pathlib


def get_file_info(file_path):
    file = pathlib.PurePosixPath(file_path.strip())
    path = file.parent.__str__()
    if path == '.':
        path = ''
    else:
        path += '/'

    file_name = file.stem.__str__()
    extension = file.suffix.__str__()

    if extension == '':
        extension, file_name = '.' + file_name, ''

    return path, file_name, extension


