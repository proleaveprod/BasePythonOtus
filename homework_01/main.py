import phonebook

FILEPATH = "phonebook.json"

book = phonebook.PhoneBook()
book.load(FILEPATH)

def main_menu():
    print("=============================")
    print("Всратый телефонный справочник")
    print("=============================")

    while True:
        print()
        print("Выберите действие:")
        print("1 - Показать все контакты")
        print("2 - Создать новый контакт")
        print("3 - Найти контакт по ключу")
        print("4 - Изменить контакт")
        print("5 - Удалить контакт")
        print("0 - Завершить работу")
        choise = None
        while 1:
            try:
                choise = int(input("Выбор: "))
                if choise in range(1,6) or choise == 0:
                    break
            except:
                print("Ошибка: недопустимый формат ответа")
            else:
                print("Ошибка: нет в списке")

        if choise == 0:
            break
        
        # Вывод списка всех контактов
        elif choise == 1:
            menu_get_contacts()

        # Создание нового контакта
        elif choise == 2:
           menu_add_new_contact()   

        # Поиск контактов по ключу
        elif choise == 3:
            menu_find_contact()

        # Измениение существующего контакта
        elif choise == 4:
            menu_change_contact()
        
        # Удаление существующего контакта
        elif choise == 5:
            menu_remove_contact()
        
def menu_get_contacts():
    print("=====================")
    print("Список всех контактов")
    print()
    for contact in book.contacts:
        contact.print()

def menu_add_new_contact():
    print("========================")
    print("Создание нового контакта")
    print()

    new_contact = phonebook.Contact()
    while True:
        new_contact.name = input("Имя контакта: ")
        
        if new_contact.name == "":
            print("Ошибка: Имя - обязательное поле")
            continue
        if book.find(new_contact.name, byName=True):
            print("Ошибка: Контакт уже существует")
            continue
        break

    new_contact.phone = input("Номер телефона: ")    
    new_contact.desc = input("Описание: ")
    new_contact.group = input("Группа: ")
    
    book.add(new_contact)
    book.save(FILEPATH)
    print(f"Контакт {new_contact.name} успешно добавлен")

def menu_find_contact():
    print("========================")
    print("Поиск контактов по ключу")
    print()
    while True:
        key = input("Ключ поиска: ")
        if key == "":
            print("Ошибка: Введите хоть что-то")
            continue
        break
    contacts = book.find(key)
    print(f"Найдено {len(contacts)} контактов:\n")
    for contact in contacts:
        contact.print()

def menu_change_contact():
    print("========================")
    print("Редактирование контакта")
    print()
    while True:
        name = input("Введите имя контакта (для выхода оставьте поле пустым): ")
        if name == "":
            return
        contact = book.find(name,byName=True)
        if contact:
            contact = contact[0]
        if contact:
            break
        else:
            print("Ошибка: Нет такого контакта")
            break
    
    print("Выберите что необходимо изменить:")
    print("1 - Имя")
    print("2 - Номер")
    print("3 - Описание")
    print("4 - Группа ")
    print("5 - Все данные")
    print("0 - Выход")
    change_choise = None
    while 1:
        try:
            change_choise = int(input("Выбор: "))
            if change_choise in range(1,6) or change_choise == 0:
                print()
                break
        except:
            print("Ошибка: недопустимый формат ответа")
        else:
            print("Ошибка: нет в списке")
    
    if change_choise == 0:
        return 

    new_contact_data = contact.get_contact_data()
    if change_choise == 1:
        new_contact_data['name'] = input(f"Старое имя: {contact.name}\nНовое имя:  ")
    elif change_choise == 2:
        new_contact_data['phone'] = input(f"Старый номер: {contact.phone}\nНовый номер:  ")
    elif change_choise == 3:
        new_contact_data['desc'] = input(f"Старое описание: {contact.desc}\nНовое описание:  ")
    elif change_choise == 4:
        new_contact_data['group'] = input(f"Старая группа: {contact.group}\nНовая группа:  ")
    elif change_choise == 5:
        new_contact_data['name'] = input(f"Старое имя: {contact.name}\nНовое имя:  ")
        new_contact_data['phone'] = input(f"Старый номер: {contact.phone}\nНовый номер:  ")
        new_contact_data['desc'] = input(f"Старое описание: {contact.desc}\nНовое описание:  ")
        new_contact_data['group'] = input(f"Старая группа: {contact.group}\nНовая группа:  ")
    
    book.remove(contact)
    book.add(new_contact_data)
    print(f"Контакт {book.contacts[-1].name} успешно изменен\n")
    book.save(FILEPATH)

def menu_remove_contact():
    print("========================")
    print("Удаление контакта")
    print()
    while True:
        name = input("Введите имя контакта (для выхода оставьте поле пустым): ")
        if name == "":
            return
        contact = book.find(name,byName=True)
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