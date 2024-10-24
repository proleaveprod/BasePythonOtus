import phonebook

FILEPATH = "phonebook.json"

book = phonebook.PhoneBook()
book.load(FILEPATH)

def main_menu():
    print("=============================")
    print("Всратый телефонный справочник")
    print("=============================")

    while True:

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
        
        # --------------------------------------------
        # Вывод списка всех контактов
        elif choise == 1:
            print("=====================")
            print("Список всех контактов")
            for contact in book.contacts:
                print(f"Имя:      {contact.name}")
                print(f"Номер:    {contact.phone}")
                print(f"Описание: {contact.desc}")
                print(f"Группа:   {contact.group}")
                print("-----------------")

        # --------------------------------------------
        # Создание нового контакта
        elif choise == 2:
            print("========================")
            print("Создание нового контакта")
            
            name = ""
            while True:
                name = input("Имя контакта: ")
                
                if name == "":
                    print("Ошибка: Имя - обязательное поле")
                    continue
                if book.find(name, byName=True):
                    print(name)
                    print("Ошибка: Контакт уже существует")
                    continue
                break
            phone = ""
            while True:
                allowed_symbol = '0123456789+-()'
                phone = input("Номер телефона: ")
                
                # NOTE: Проверка валидности только по разрешенным символам. Однако нет проверки на подобный номер: +++7---911((()))-((124-42-11--   
                invalid_flag = False
                for c in phone:
                    if c not in allowed_symbol:
                        print(f"Ошибка: Недопустимый символ {c}")
                        invalid_flag = True
                        break
                if invalid_flag == False:
                    break
                
            desc = input("Описание: ")
            group = input("Группа: ")
            
            contact_data = {
                "name": name,
                "phone": phone,
                "desc": desc,
                "group": group
            }
            book.add(contact_data)
            book.save(FILEPATH)
            print(f"Контакт {name} успешно добавлен")   

        # --------------------------------------------
        # Поиск контактов по ключу
        elif choise == 3:
            print("========================")
            print("Поиск контактов по ключу")
            while True:
                key = input("Ключ поиска: ")
                if key == "":
                    print("Ошибка: Введите хоть что-то")
                    continue
                break
            contacts = book.find(key)
            print(f"Найдено {len(contacts)} контактов:\n")
            for contact in contacts:
                print(f"Имя:      {contact.name}")
                print(f"Номер:    {contact.phone}")
                print(f"Описание: {contact.desc}")
                print(f"Группа:   {contact.group}")
                print("-----------------")



main_menu()