from pprint import pprint
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
    fio = contact[0].split(" ")
    if len(fio) > 1:
        contact[0] = fio[0]
        contact[1] = fio[1]
    if len(fio) > 2:
        contact[2] = fio[2]

# pprint(contacts_list)

# Task 3

for i in range(1, len(contacts_list)):
    for j in range(i + 1,len(contacts_list)):
        if contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1]:
            contacts_list[i] = [x if x else y for x, y in zip(contacts_list[i], contacts_list[j])]
            contacts_list[j] = contacts_list[i]

result_set = set()
contacts_list = [x for x in contacts_list if tuple(x) not in result_set and not result_set.add(tuple(x))]

print(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)



# for i in range(1, len(contacts_list)):
#     print("\n\ni = " + str(i))
#     print("==================================")
#     for j in range(i + 1,len(contacts_list)):
#         print("j = " + str(j))
#         if contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1]:
#             print(contacts_list[i],contacts_list[j])
#             contacts_list[i] = [x if x else y for x, y in zip(contacts_list[i], contacts_list[j])]
#             contacts_list[j] = contacts_list[i]
#             print(contacts_list[i],contacts_list[j])
#
# result_set = set()
# contacts_list = [x for x in contacts_list if tuple(x) not in result_set and not result_set.add(tuple(x))]

# for i in range(len(contacts_list)):
#     for j in range(1, len(contacts_list)):
#         print(str(i) + ";" + str(j))

# for i, contact in enumerate(contacts_list[1:]):
#     print("\n\ni = " + str(i))
#     print("contact = " + str(contact))
#     print("==================================")
#     for j, item in enumerate(contacts_list[i+1:]):
#         print("j = " + str(j))
#         if contact[0] == item[0]:
#             print(i,contact)


# for contact in contacts_list[1:]:
#     print("\n\ncontact = " + str(contact[0]))
#     print("==================================")
#     for item in contacts_list[contacts_list.index(contact) + 1:]:
#         print("item = " + str(item[0]))
#         if contact[0] == item[0]:
#             print(contact,item)

# print(contacts_list)
#
# for contact in contacts_list[1:]:
#     print("\n\ncontact index = " + str(contacts_list.index(contact)) + " contact = " + str(contact[0]))
#     print("==================================")
#     for item in contacts_list[contacts_list.index(contact) + 1:]:
#         print("item index = " + str(contacts_list.index(item)) + " item = " + str(item[0]))
#         if contact[0] == item[0] and contact[1] == item[1]:
#             print(contact,item)
#             contact = [x if x else y for x, y in zip(contact, item)]
#             print(contact, item)
#             # contacts_list.remove(item)
#
# print(contacts_list)

# for i, contact in enumerate(contacts_list[1:]):
#     print("\n\ni = " + str(i) + " contact index = " + str(contacts_list.index(contact)) + " contact = " + str(contact[0]))
#     print("==================================")
#     for j, item in enumerate(contacts_list[contacts_list.index(contact) + 1:]):
#         print("j = " + str(j) + " item index = " + str(contacts_list.index(item)) + " item = " + str(item[0]))
#         if contact[0] == item[0] and contact[1] == item[1]:
#             print(contact,item)
#             contacts_list[i+1] = [x if x else y for x, y in zip(contact, item)]
#             print(contact, item)
#             # del (contacts_list[contacts_list.index(item)])
#             # contacts_list.remove(item)
#
# print(contacts_list)