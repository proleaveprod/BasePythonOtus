from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from modules.schemas import Character, Side

from modules.database import characters

router = APIRouter(prefix="/api")

@router.get('/character', 
         name='Получить всех персонажей',
         tags=['api'])
async def get_characters():
    return characters.get_all()

@router.get('/character/{id}', 
         name='Получить персонажа по id',
         tags=['api'])
async def get_character(id: int):
    return characters.get(id)


@router.post('/character', 
         name='Добавить нового персонажа',
         tags=['api'])
async def post_character(new_character: Character):
    return characters.add(new_character)


@router.put('/character/{id}', 
         name='Полное обновление данных персонажа по id',
         tags=['api'])
async def put_character(id: int, updated_character: Character):
    return characters.update(id, updated_character, patch=False)


@router.patch('/character/{id}', 
         name='Дополнение или правка данных персонажа по id',
         tags=['api'])
async def patch_character(id: int, updated_character: Character):
    return characters.update(id, updated_character, patch=True)


@router.delete('/character/{id}', 
         name='Удалить персонажа по id',
         tags=['api'])
async def delete_character(id: int):
    return characters.delete(id)