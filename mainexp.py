from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
import re
new_contacts_list = []
for row in contacts_list:
    for column in range(2):
      pattern = r"\w+"
      name_list = re.findall(pattern, row[column])
      row[column] = name_list.pop(0)
      if name_list:
        row[column + 1] = ' '.join(name_list)

    pattern_ph = r"(\+7|8)?\s*\(*(\d+)\)*\s*(\d+)[-\s]+(\d+)[-\s](\d+)(\W*(доб.\s*\d+)\)*)?"
    if row[5] != "phone":
      result = re.sub(pattern_ph, r"+7(\2)\3-\4-\5\6", row[5])
      row[5] = result
    new_contacts_list.append(row[:7])

#print(new_contacts_list)

final_list = []
while new_contacts_list:
  base_row = new_contacts_list.pop(0)
  for row in reversed(new_contacts_list):
    if row[0:1] == base_row[0:1]:
      for cell in range(len(row)):
        if row[cell] != base_row[cell]:
          base_row[cell] = base_row[cell] + row[cell]
      new_contacts_list.remove(row)
  final_list.append(base_row)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
pprint(final_list)
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(final_list)
