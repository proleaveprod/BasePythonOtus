from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter

from config import templates
from models import crud
from models import engine, Session


router = APIRouter(prefix="")

# Обработчик главной страницы с карточками персонажей
@router.get('/', response_class=HTMLResponse, 
         name='Главная страница',
         description='Страница с персонажами из комиксов',
         tags=['view'])
async def get_index(request: Request):
    page = 'index'
    
    with Session(engine) as session:
        characters = crud.get_all_characters(session)
    
    context = {
        "request": request,
        "current_page": page,
        "characters": characters
    }
    return templates.TemplateResponse(f'{page}.html', context)


# Обработчик страницы "О проекте"
@router.get('/about', response_class=HTMLResponse,
         name='О проекте',
         description='Описание проекта, информация об авторе',
         tags=['view']) 
async def get_about(request: Request):
    page = 'about'
    context = {
        "request": request,
        "current_page": page
    }
    return templates.TemplateResponse(f'{page}.html', context)


# Обработчик страницы с информацией об API
@router.get('/api', response_class=HTMLResponse, 
         name='Информация об API',
         description='Страница об использовании API проекта',
         tags=['view'])
async def get_api_info(request: Request):
    page = 'api'
    context = {
        "request": request,
        "current_page": page
    }
    return templates.TemplateResponse(f'{page}.html', context)