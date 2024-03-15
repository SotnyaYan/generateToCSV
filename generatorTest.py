import csv
import random

def random_choice(choices):
    return random.choice(choices)

def gen_id():
    return '12' + ''.join(str(random.randint(0,9)) for _ in range(15))
def gen_inn():
    return ''.join(str(random.randint(0,9)) for _ in range(12))
def gen_kpp():
    return ''.join(str(random.randint(0,9)) for _ in range(9))

gen_name = ['STATE_SOURCES', 'INNER_BANK_SOURCES', 'COMPLIANCE', 'SBER_RATING_TOTAL']
gen_color = ['G', 'Y', 'R', 'B']
def generator(file):
    num_rows = random.randint(1, 50)

    data = []
    for _ in range(num_rows):
        id = gen_id()
        inn = gen_inn()
        kpp = gen_kpp()
        name = random_choice(gen_name)
        color = random_choice(gen_color)
        translation_allowed = random_choice([0, 1])
        is_priority = random_choice([0, 1])

        data.append([id, inn, kpp, name, color, translation_allowed, is_priority])

    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['id', 'inn', 'kpp', 'name', 'color', 'translation_allowed', 'is_priority'])

        for row in data:
            writer.writerow(row)

        rows_with_data_count = len(data)

        csvfile.write(f"Количество строк: {rows_with_data_count}")

generator('sberrating.csv')
