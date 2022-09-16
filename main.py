import regex as re
import csv
import models

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

@models.foo_logger(models.log_file)
def phone_pattern(contact:dict):
    '''Приводит номер телефона к единому виду: +7(999)999-99-99 доб.9999'''
    pattern = r"(\+7|8)\s?\(?(\d{3})\)?[\s\-]?(\d{3})\-?(\d{2})\-?(\d{2})\s?(\(?((доб.)\s(\d+))\)?)?"
    repl = r'+7(\2)\3-\4-\5 \8\9'
    result = re.sub(pattern, repl, contact.get('phone'))
    contact.update(phone = result.strip())
    return contact

@models.foo_logger(models.log_file)
def initials(contact:dict):
    '''Распаковывает ФИО по полям: lastname, firstname, surname'''
    text = ' '.join([contact.get('lastname'), contact.get('firstname'), contact.get('surname')])
    list_initials = text.split()
    contact.update(lastname = list_initials.pop(0), firstname = list_initials.pop(0))
    if list_initials:
        contact.update(surname = list_initials.pop(0))
    return contact

@models.foo_logger(models.log_file)
def filter(contact:dict):
    '''Сравнивает записи для поиска дублей по ФИ,
        если находит совпадение - обновляет запись новыми данными
        если не находит совпадение - добавляет новую запись'''
    filtered = dict((k, v) for k, v in contact.items() if v)
    if facebook:
        for num, i in enumerate(facebook):
            equal_lastname = filtered.get('lastname') == i.get('lastname')
            equal_firstname = filtered.get('firstname') == i.get('firstname')
            if equal_lastname and equal_firstname:
                facebook[num].update(filtered)
                break
        else:
            facebook.append(contact)
    else:
        facebook.append(contact)
    return


if __name__ == '__main__':

    facebook = []

    with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        contacts_list = list(rows)
        fieldnames = rows.fieldnames

    for contact in contacts_list:
        # first = initials(contact)
        # second = phone_pattern(first)
        # third = filter(second)
        filter(phone_pattern(initials(contact)))

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.DictWriter(f, fieldnames, lineterminator='\n', extrasaction='ignore')
    # Вместо contacts_list подставьте свой список
        datawriter.writeheader()
        datawriter.writerows(facebook)