code = """import csv
import json
import random
import math


def save_to_json(func):
    def wrapper(*args):
        csv_file = args[0]
        results = {}

        with open(csv_file, mode='r') as file:
            data = csv.reader(file)
            for i, row in enumerate(data):
                a, b, c = map(int, row)
                results[f'{i}. {a}x^2 + {b}x + {c} = 0'] = func(a, b, c)

        with open('results.json', 'w') as file:
            json.dump(results, file)

    return wrapper


def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            writer.writerow([random.randint(1, 100) for _ in range(3)])


@save_to_json
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)

        return x1, x2
    elif discriminant == 0:
        return (-b + math.sqrt(discriminant)) / (2*a)
    else:
        return None

"""

with open('__init__.py', 'w') as file:
    file.write(code)