from fastapi import APIRouter
from models import engine, Session, crud, schemas
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api")

@router.get('/characters/', 
         name='Получить всех персонажей',
         tags=['api'])
async def get_characters():
    with Session(engine) as session:
        character_list = crud.get_all_characters(session)
    
    return character_list

@router.get('/characters/{id}', 
         name='Получить персонажа по id',
         tags=['api'])
async def get_character(id: int):
    with Session(engine) as session:
        character = crud.get_character(session, id)
        if character:
            return character
    return {"POSOSI": 123}

@router.post("/characters/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate):
    # Проверяем, существует ли уже персонаж с таким именем
    
    with Session(engine) as session:
        
        db_character = crud.get_character_by_name(session, name=character.name)
        if db_character:
            raise HTTPException(
                status_code=400, 
                detail="Персонаж с таким именем уже существует"
            )
    
        return crud.create_character(session, character=character)