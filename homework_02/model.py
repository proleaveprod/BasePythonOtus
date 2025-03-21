from dataclasses import dataclass,asdict
import json

@dataclass
class Contact:
    name: str
    phone: str
    desc: str
    group: str

class PhoneBook:
    def __init__(self, path: str):
        """
        :param path: Путь к json-файлу справочника
        """
        self.contacts = list()
        self.path = path
        self.load()

    def load(self):
        """
        Загрузить контакты из json-файла
        :param path: Путь к json-файлу
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data_list = json.load(file)
            for data in data_list:
                contact = Contact(**data) # Распаковка словаря в dataclass
                self.contacts.append(contact)

            self.contacts.sort(key=lambda x: x.name) # Сортировка по имени


    def save(self):
        """
        Сохранение телефонной книги в файл
        """

        # Предварительная сортировка по имени
        self.contacts.sort(key=lambda x: x.name)

        # Преобразование объектов в словари
        data_to_save = list()
        for contact in self.contacts:
            contact_data = asdict(contact)
            data_to_save.append(contact_data)

        # Сохранение json
        with open(self.path, 'w', encoding='utf-8') as file:
            json_object = json.dumps(data_to_save, ensure_ascii=False, indent=2)
            file.write(json_object)

    def add(self, contact: Contact):
        """
        Добавление нового контакта
        :param contact: Новый контакт
        """
        self.contacts.append(contact)

    def remove(self, contact: Contact):
        """
        Удаление контакта
        :param contact: Контакт, который нужно удалить
        """
        self.contacts.remove(contact)

    def change(self, old: Contact, new: Contact):
        """
        Изменение контакта
        :param old: Первоначальный контакт
        :param new: Его измененная версия
        """

    def find(self, key: str, only_name = False):
        """
        Поиск контактов по ключу. Выполняется либо по всем полям объектов Contact, либо только по name
        В первом случае при удачном поиске функция вернет список объектов, во втором один объект
        :param key: Ключ поиска
        :param only_name: Флаг поиска только по имени (True/False)
        :return: а) Список объектов Contact; б) Уникальный объект, если поиск с флагом only_name = True.
        """
        # Поиск только по имени. Т.к. имя в словаре уникально, возвращаем не список, а 1 Contact
        if only_name:
            for contact in self.contacts:
                if contact.name == key:
                    return contact
            return None

        # Поиск по всем полям.
        found_list = list()
        for contact in self.contacts:
            if contact.name.lower().find(key.lower()) != -1:
                pass
            elif contact.name.lower().find(key.lower()) != -1:
                pass
            elif contact.phone.lower().find(key.lower()) != -1:
                pass
            elif contact.desc.lower().find(key.lower()) != -1:
                pass
            elif contact.group.lower().find(key.lower()) != -1:
                pass
            else:
                continue
            found_list.append(contact)

        return found_list if len(found_list) > 0 else None

