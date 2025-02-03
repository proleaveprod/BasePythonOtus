from pydantic import BaseModel, Field
from typing import Annotated
from classes import *


class Character(BaseModel):
    """
    Класс для персонажей комиксов

    Обязательные поля: 
      1) id - уникальный идентификатор персонажа
      2) name - имя персонажа
      3) side - сторона света
    
    Необязательные поля:
      1) fullname - полное имя
      2) desc - краткое описание
      3) powers- способности
      4) img_url - ссылка на фото для карточки
    """
    id: Annotated[int, Field(...)]
    name: Annotated[str, Field(..., max_length=20)]
    side: Annotated[Side, Field(...)]

    fullname: Annotated[str, Field(None, max_length=60)]
    desc: Annotated[str, Field(None, max_length=300)]
    powers: Annotated[list[str], Field(None)]
    img_url: Annotated[str, Field(None)]
