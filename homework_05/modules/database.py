"""
Способ хранения данных о персонажах - json файл
"""

import json
from modules.schemas import Character, Side

class CharacterBook():
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.characters = list()

        # Чтение json-файла и запись в список characters_data 
        characters_data = list()
        with open(filepath,'r+',encoding='utf-8') as f:
            characters_data = json.load(f)

        for data in characters_data:
            character = Character.model_validate(data)
            self.characters.append(character) # Вычитываем данные из json и пополняем спискок characters объектами Character
    
    def save(self):
        """
        Сохранение списка self.characters в json-файл
        """

        # character.model_dump(mode="json") для автоматической сериализации Enum. 
        # В противном случае model_dump выдаст для ключа "side": <Side.good: 'Добро'>
        data_to_save = [character.model_dump(mode="json", exclude_none=True) for character in self.characters] 
        with open(self.filepath, "w", encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)

    def get(self, id: int):
        for character in self.characters:
            if character.id == id:
                return {'status': 'OK', 'details': 'Character is found', 'data': character.model_dump()}

        return {'status': 'ERROR', 'details': 'Character is not found'}

    def add(self, new_character: Character):

        # Проверка занятости ID 
        for character in self.characters:
            print(f"{character.name}: {character.id}")
            if character.id == new_character.id:
                return {'status': 'ERROR', 'details': 'The ID is already occupied'}

        self.characters.append(new_character)
        self.save()

        return {'status': 'OK', 'details': 'Successfully added'}

    def delete(self, id: int):
        for character in self.characters:
            if character.id == id:
                self.characters.remove(character)
                self.save()
                return {'status': 'OK', 'details': 'Successfully deleted'}
        return {'status': 'ERROR', 'details': 'The ID is not found'}

    def update(self, id: int, updated_character: Character, patch: bool = False):
        """
        Обновление персонажа по id
        Аргументы:
        1)id - Идентификатор персонажа
        2)updated_character - Объект, которым заменяем первоначальный
        3)patch - Флаг слияния первоначального и нового объекта (метод patch). 
        Все поля character, которых нет в new_character, будут оставлены как есть.

        TODO WARNING: Небезопасно то, что я могу поставить id = 1, а в updated_character.id = 2.
        Если уже существует персонаж с id=2, тогда я сделаю 2 записи с id 2. При правке id=2 мы потеряем одну из записей.
        Из-за этого придется удалять обе и делать заново запись. 

        Вопрос куратору: Как по-умному это можно регулировать?
        1) Использовать базу данных, да, но я хотел именно по json всё сделать, т.к. интересен такой формат
        2) Делать еще 1 цикл внутри функции, которая проверяет, что updated_character.id не занят (исключение - сам аргумент id)
        Но это же дополнительная работа. Если будет 10к записей, то не очень... 
        3) Хранить пул незанятых id?
        Есть идеи еще?
        """
        for i, character in enumerate(self.characters):
            if character.id == id:
                updated_data = updated_character.model_dump(exclude_unset=patch) 
                self.characters[i] = character.model_copy(update=updated_data)
                self.save()
            
                return {'status': 'OK', 'details': 'Successfully updated'}
            
        return {'status': 'ERROR', 'details': 'The ID is not found'}

    def get_all(self):
        datalist = list()
        for character in self.characters:
            datalist.append(character.model_dump())

        return {'status': 'OK', 'details': 'All characters', 'data': datalist}



characters = CharacterBook('database.json')