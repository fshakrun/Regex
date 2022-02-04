import re
from pprint import pprint
import csv
import codecs


PHONE_FORMAT = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUBST = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ

def main(contact_list: list):
    updated_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        results = [full_name[0],
                   full_name[1],
                   full_name[2],
                   item[3],
                   item[4],
                   re.sub(PHONE_FORMAT, PHONE_SUBST, item[5]),
                   item[6]], \
            updated_list.append(results)
    return union(updated_list)


def union(entries: list):
    #обрабатываем список
    for contact in entries:
        first_name = contact[0]
        last_name = contact[1]
        for upd_contact in entries:
            new_first_name = upd_contact[0]
            new_last_name = upd_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = upd_contact[2]
                if contact[3] == "": contact[3] = upd_contact[3]
                if contact[4] == "": contact[4] = upd_contact[4]
                if contact[5] == "": contact[5] = upd_contact[5]
                if contact[6] == "": contact[6] = upd_contact[6]

    results_list = list()
    for e in entries:
        if e not in results_list:
            results_list.append(e)

    return results_list


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(results_list)