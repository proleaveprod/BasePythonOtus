from fastapi import APIRouter
from modules.routers.character import router as character_router
from modules.database import characters

router = APIRouter(prefix="/api")
router.include_router(character_router)  

@router.get('/characters', 
         name='Получить всех персонажей',
         tags=['api'])
async def get_characters():
    return characters.get_all()



