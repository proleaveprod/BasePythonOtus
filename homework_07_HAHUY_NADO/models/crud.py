from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from . import schemas
from .character import Character
from .power import Power
from .base import engine

def get_character(session: Session, id: int) -> Character:
    character = session.get(Character, id)
    return character

def get_all_characters(session: Session) -> list[Character]:
    stmt = (
        select(Character)
        .options(
            selectinload(Character.powers)
        )
        .order_by(Character.id)
    )
    characters = session.scalars(stmt).all()
    
    return characters

def create_character(session: Session, character: schemas.CharacterCreate):
    # Создаем персонажа
    db_character = Character(
        name=character.name,
        fullname=character.fullname,
        desc=character.desc,
        img_url=character.img_url
    )
        
    # Обрабатываем способности
    for power in character.powers:
        # Проверяем, существует ли уже такая способность
        db_power = session.query(Power).filter(Power.name == power.name).first()
        if not db_power:
            # Если не существует, создаем новую
            db_power = Power(name=power.name)
            session.add(db_power)
            session.flush()  # Чтобы получить ID новой способности
            
        # Добавляем связь между персонажем и способностью
        db_character.powers.append(db_power)
    
    session.add(db_character)
    session.commit()
    session.refresh(db_character)

    return db_character

def get_character_by_name(session: Session, name: str):
    return session.query(Character).filter(Character.name == name).first()