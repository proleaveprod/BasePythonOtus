from typing import TYPE_CHECKING
from enum import Enum as PyEnum

from sqlalchemy import String, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, CreatedTimeStamp
from .character_power import character_power

if TYPE_CHECKING:
    from . import Power

class Character(CreatedTimeStamp, Base):
    __tablename__ = 'characters'
    
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    fullname: Mapped[str] = mapped_column(String(100), nullable=True, unique=False)
    desc: Mapped[str] = mapped_column(Text, nullable=True, unique=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True, unique=False)
    
    # many-to-many
    powers: Mapped[list["Power"]] = relationship(
        "Power", 
        secondary=character_power,  # указываем ассоциативную таблицу
        back_populates="characters" # имя обратной связи в модели Power
    )
    
    def __str__(self):
        return f"{self.__class__.__name__} №{self.id}. {self.name}"