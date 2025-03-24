from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .character_power import character_power

if TYPE_CHECKING:
    from . import Character
    
    
class Power(Base):
    __tablename__ = 'powers'
    
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    # many-to-many
    characters: Mapped[list["Character"]] = relationship(
        "Character", 
        secondary=character_power,  # указываем ассоциативную таблицу
        back_populates="powers"     # имя обратной связи в модели Power
    )
    
    def __str__(self):
        return f"{self.__class__.__name__} №{self.id}. {self.name}"