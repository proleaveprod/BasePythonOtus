"""
Способ хранения данных о персонажах - json файл
"""

import json
from schemas import Character

class CharacterBook():
    def __init__(self, filepath: str):
        with open(filepath,'r+',encoding='utf-8') as f:
            characters_data = json.load(f)

            self.characters = []

            character = Character.model_validate(characters_data[0])

            print(character)

        



a = CharacterBook('database/database.json')