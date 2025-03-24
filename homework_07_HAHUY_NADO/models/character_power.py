from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

# Ассоциативная таблица для связи many-to-many
character_power = Table(
    'characters_powers',  # имя таблицы в БД
    
    Base.metadata,      # базовый метаданный
    Column('character_id', Integer, ForeignKey('characters.id'), primary_key=True),
    Column('power_id', Integer, ForeignKey('powers.id'), primary_key=True)
)