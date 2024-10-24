import json 

class Contact():
    def __init__(self, contact_dict):
        self.phone = contact_dict['phone']
        self.name  = contact_dict['name']
        self.desc  = contact_dict['desc']
        self.group = contact_dict['group']

class PhoneBook():
    def __init__(self):
        self.contacts = list()

    # Выгрузить json-словарь из справочника
    def load(self, path):
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for contact_data in data:
                    self.contacts.append(Contact(contact_data)) # Заполняем справочник объектами класса Contact
                self.contacts.sort(key = lambda x: x.name)

    # Сохранить json-словарь в справочник
    def save(self, path):
        self.contacts.sort(key = lambda x: x.name)

        data_to_save = list()
        for contact in self.contacts:
            contact_data = {
                    "name": contact.name,
                    "phone": contact.phone,
                    "desc": contact.desc,
                    "group": contact.group
            }
            
            data_to_save.append(contact_data)
            with open(path,'w',encoding='utf-8') as file:
                json_object = json.dumps(data_to_save, ensure_ascii=False, indent=4)
                file.write(json_object)

    # Найти контакт по ключу
    def find(self, key, byName=False):
        found_list = list()
        for contact in self.contacts:
            if byName == True:
                if key == contact.name:
                    pass
                continue
            else:
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
        
        return found_list
    
    def get_contact_idx(self, contact):
        idx = self.contacts.index(contact)
        return idx

    def add(self, contact_data):
        self.contacts.append(Contact(contact_data))

    def remove(self, contact):
        self.contacts.remove(contact)        

    def change(self, contact, new_contact_data):        
        if contact in self.contacts:
            print("Huy")
