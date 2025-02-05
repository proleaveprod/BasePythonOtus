from pydantic import BaseModel, Field
from typing import Annotated

from modules.classes import Side

class Character(BaseModel):
    """
    Класс для персонажей комиксов

      1) id - уникальный идентификатор персонажа - Обязательное поле
      2) name - имя персонажа
      3) side - сторона света
      4) fullname - полное имя
      5) desc - краткое описание
      6) powers- способности
      7) img_url - ссылка на фото для карточки
    """
    id: Annotated[int, Field(...)]
    name: Annotated[str, Field(None, max_length=20)]
    side: Annotated[Side, Field(None)]

    fullname: Annotated[str, Field(None, max_length=60)]
    desc: Annotated[str, Field(None, max_length=300)]
    powers: Annotated[list[str], Field(None)]
    img_url: Annotated[str, Field(None)]
