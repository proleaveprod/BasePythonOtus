from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from common import *
from schemas import Character, Side

router = APIRouter(prefix="/api")

characters = []
characters.append(Character(id=1,name="Ебан",side=Side.evil))
characters.append(Character(id=2,name="Сасан",side=Side.evil))



# Обработчик получения json-данных о персонаже по id
@router.get('/character/{id}', 
         name='Получить персонажа по id',
         tags=['api'])
async def get_character(id: int):
    for c in characters:
        
    return {"sasi": "guboy tryasi"}