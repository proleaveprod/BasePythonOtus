from model import PhoneBook
from view import View

class PhonebookController:
    def __init__(self):
        self.model = PhoneBook('phonebook.json')
        self.view = View()

    def start(self):
        self.view.start_message()
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Выберите опцию: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.remove_contact()
            elif choice == "3":
                self.find_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                break
            else:
                self.view.show_message("Неверный выбор, попробуйте снова.")

    def add_contact(self):
        phone = self.view.get_input("Введите телефон: ")
        name = self.view.get_input("Введите имя: ")
        desc = self.view.get_input("Введите описание: ")
        group = self.view.get_input("Введите группу: ")
        contact = Contact(phone, name, desc, group)
        self.model.add_contact(contact)
        self.view.show_message("Контакт добавлен.")

    def remove_contact(self):
        phone = self.view.get_input("Введите телефон для удаления: ")
        self.model.remove_contact(phone)
        self.view.show_message("Контакт удален.")

    def find_contact(self):
        phone = self.view.get_input("Введите телефон для поиска: ")
        contact = self.model.find_contact(phone)
        self.view.show_contact(contact)

    def update_contact(self):
        phone = self.view.get_input("Введите телефон для изменения: ")
        contact = self.model.find_contact(phone)
        if contact:
            name = self.view.get_input(f"Новое имя (текущее: {contact.name}): ")
            desc = self.view.get_input(f"Новое описание (текущее: {contact.desc}): ")
            group = self.view.get_input(f"Новая группа (текущая: {contact.group}): ")
            self.model.update_contact(phone, name, desc, group)
            self.view.show_message("Контакт обновлен.")
        else:
            self.view.show_message("Контакт не найден.")
