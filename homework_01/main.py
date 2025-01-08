import phonebook

FILEPATH = "phonebook.json"

book = phonebook.PhoneBook()
book.load(FILEPATH)


def main_menu():
    """
    Функция главного меню
    Здесь принимаем выбор действия через ввод с клавиатуры
    """

    print("=============================")
    print("Всратый телефонный справочник")
    print("=============================")

    while True:
        print("1 - Показать все контакты")
        print("2 - Создать новый контакт")
        print("3 - Найти контакт по ключу")
        print("4 - Изменить контакт")
        print("5 - Удалить контакт")
        print("0 - Завершить работу")

        a = input('Выберите действие: ')
        if a.isdigit():
            idx = int(a)
            if idx == 0:  # Выход из программы
                break
            elif idx == 1:  # Вывод списка всех контактов
                menu_get_contacts()
            elif idx == 2:  # Создание нового контакта
                menu_add_new_contact()
            elif idx == 3:  # Поиск контактов по ключу
                menu_find_contact()
            elif idx == 4:  # Изменение существующего контакта
                menu_change_contact()
            elif idx == 5:  # Удаление существующего контакта
                menu_remove_contact()
            else:
                print("Ошибка: Нет такого действия.")
        else:
            print("Ошибка: Введите число.")


def menu_get_contacts():
    """
    Вывод списка всех контактов в терминал
    """

    print("=====================")
    print("Список всех контактов")
    print()
    for contact in book.contacts:
        contact.print()


def menu_add_new_contact():
    """
    Добавление нового контакта в таблицу
    Имя контакта должно быть уникальным и не должно быть пустым
    """

    print("========================")
    print("Создание нового контакта")
    print()

    new_contact = phonebook.Contact()
    while True:
        new_contact.name = input("Имя контакта:")

        if new_contact.name == "":
            print("Ошибка: Имя - обязательное поле")
            continue
        if book.find(new_contact.name, byName=True):
            print("Ошибка: Контакт уже существует")
            continue
        break  # При корректном вводе имени нового контакта сразу выйдем из данного цикла

    new_contact.phone = input("Номер телефона: ")
    new_contact.desc = input("Описание: ")
    new_contact.group = input("Группа: ")

    book.add(new_contact)
    book.save(FILEPATH)
    print(f"Контакт {new_contact.name} успешно добавлен")


def menu_find_contact():
    """
    Поиск контакта по определенному ключу
    Ключом может быть любое поле класса Contact.
    """

    print("========================")
    print("Поиск контактов по ключу")
    print()

    key = input("Ключ поиска (для отмены оставьте поле пустым): ")
    if key == "":
        return

    contacts = book.find(key)

    if len(contacts) > 0:
        # Вывод.
        print(f"Найдено {len(contacts)} контактов:\n")
        for contact in contacts:
            contact.print()
    else:
        print("Таких контактов не найдено")


def menu_change_contact():
    """
    Изменение контакта по заданному имени
    Можно изменить любое поле или все вместе
    """
    print("========================")
    print("Редактирование контакта")
    print()

    name = input("Введите имя контакта (для отмены оставьте поле пустым): ")
    if name == "":
        return

    contact = book.find(name, byName=True)
    if contact:
        contact = contact[0]
    else:
        print("Ошибка: Нет такого контакта")
        return

    while True:
        print(f"Изменение контакта {name}")
        print("Выберите что нужно изменить:")
        print("1 - Имя")
        print("2 - Номер")
        print("3 - Описание")
        print("4 - Группа ")
        print("5 - Все данные")
        print("0 - Выход")

        a = input("Выбор: ")
        if not a.isdigit():
            print("Ошибка: Введите число")
            continue
        idx = int(a)
        if idx == 0:
            return

        new_contact_data = contact.get_contact_data()

        print(new_contact_data)

        if   idx == 1:
            new_contact_data['name'] = input(f"Старое имя: {contact.name}\nНовое имя:  ")
        elif idx == 2:
            new_contact_data['phone'] = input(f"Старый номер: {contact.phone}\nНовый номер:  ")
        elif idx == 3:
            new_contact_data['desc'] = input(f"Старое описание: {contact.desc}\nНовое описание:  ")
        elif idx == 4:
            new_contact_data['group'] = input(f"Старая группа: {contact.group}\nНовая группа:  ")
        elif idx == 5:
            new_contact_data['name'] = input(f"Старое имя: {contact.name}\nНовое имя:  ")
            new_contact_data['phone'] = input(f"Старый номер: {contact.phone}\nНовый номер:  ")
            new_contact_data['desc'] = input(f"Старое описание: {contact.desc}\nНовое описание:  ")
            new_contact_data['group'] = input(f"Старая группа: {contact.group}\nНовая группа:  ")
        else:
            print("Ошибка: Выберите действие из списка")
            continue

        new_contact = phonebook.Contact(new_contact_data)
        book.remove(contact)
        book.add(new_contact)
        book.save(FILEPATH)

        print(f"Контакт {new_contact_data['name']} успешно изменен\n")
        return


def menu_remove_contact():
    """
    Удаление контакта по заданному имени
    """
    
    print("========================")
    print("Удаление контакта")
    print()
    while True:
        name = input("Введите имя контакта (для выхода оставьте поле пустым): ")
        if name == "":
            return
        contact = book.find(name, byName=True)
        if contact:
            contact = contact[0]
        if contact:
            break
        else:
            print("Ошибка: Нет такого контакта")
            break
    contact.print()
    delete_word = input("Подтверждение удаления (введите 'да'): ")
    if delete_word == "да":
        book.remove(contact)
        book.save(FILEPATH)
        print("Контакт успешно удален")
    else:
        print("Контакт не удален")


main_menu()
