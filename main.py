from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# Task 1

for contact in contacts_list:
    fio = " ".join([s for s in [contact[0], contact[1], contact[2]] if s])
    fio_list = fio.split(" ")

    for i, item in enumerate(fio_list):
        contact[i] = fio_list[i]


# Task 2

phone_pattern = r"(8|\+7)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*)(\(?(доб\.)\)?)?\s*(\d{4})?\)?"

for contact in contacts_list:
    contact[5] = re.sub(phone_pattern, r"+7(\2)-\3-\4-\5\6\8\9", contact[5])


# Task 3

for i in range(1, len(contacts_list)):
    for j in range(i + 1,len(contacts_list)):
        if contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1]:
            contacts_list[i] = [x if x else y for x, y in zip(contacts_list[i], contacts_list[j])]
            contacts_list[j] = contacts_list[i]

result_set = set()
contacts_list = [x for x in contacts_list if tuple(x) not in result_set and not result_set.add(tuple(x))]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)


