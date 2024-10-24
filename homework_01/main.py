import json 

phonebook_path = 'phonebook.json'

class Contact():
    def __init__(self, contact_dict):
        self.phone = contact_dict['phone']
        self.name = contact_dict['name']
        self.desc = contact_dict['desc']
        self.group = contact_dict['group']

class PhoneBook():
    def __init__(self):
        self.contacts = list()

    # Открыть файл справочника
    def open(self, path):
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for contact_data in data:
                    self.contacts.append(Contact(contact_data)) # Заполняем справочник объектами класса Contact

    def save(self, path):
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

    def find(self, key):
        found_list = list()
        for contact in self.contacts:
            
            isFound = True
            
            if contact.name.find(key):
                break
            elif contact.phone.find(key):
                break
            elif contact.desc.find(key):
                break
            elif contact.group.find(key):
                break
            else:
                isFound = False
            
            if isFound:
                found_list.append(contact
                                  )



    def add(self, contact_data):
        self.contacts.append(Contact(contact_data))

    def change(self, contact, contact_data):
        self.contacts.remove(contact)

    def remove(self, contact):
        self.contacts.remove(contact)        




# print(Contact.att)

# pb = PhoneBook()
# pb.open(phonebook_path)
# pb.save(phonebook_path)

# pb.remove(2)
