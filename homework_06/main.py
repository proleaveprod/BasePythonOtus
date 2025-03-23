"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from logger import logger as log

from models import Base, async_engine, async_session_factory
from models import crud
from models import User, Post
import fetch_api

DB_LAZY_CREATOR = True  # Пересоздать таблицы users и posts в БД?
API_TIMEOUT = 1.5       # Сколько секунд ждем получение users и posts

async def database_fill():
    if DB_LAZY_CREATOR:
        await crud.create_database() # Миграции? Неее
        
    ###--------------------------------------------------------------
    # Получаем от API dict['users': list[dict], 'posts': list[dict]] 
    api_data = await fetch_api.get_users_posts_data(timeout = API_TIMEOUT) 
    if not api_data:            
        raise Exception('Не удалось получить все данные из API')
    
    # Создание ORM-объектов users   
    users = [            
        # 2. Т.к. полученные с API dict имеют огромное кол-во лишних ключей, отсеиваем только то, что нужно модели User
        User(**{key: value
                    for key, value in userdata.items() if key in User.__table__.columns})
        
        # 1. прогоняемся по всему списку из словарей api_data['users'] 
        for userdata in api_data['users']
    ]
    # Создание ORM-объектов posts
    posts = [            
        # 2. Т.к. полученные с API dict имеют огромное кол-во лишних ключей, отсеиваем только то, что нужно модели Post
        Post(**{key: value
                    for key, value in postdata.items() if key in Post.__table__.columns})
        
        # 1. прогоняемся по всему списку из словарей api_data['posts'] 
        for postdata in api_data['posts']
    ]
    
    # Сразу сортируем списки, чтобы в БД было всё по порядку id 
    users.sort(key=lambda user: user.id)
    posts.sort(key=lambda post: post.id)
            
    ###--------------------------------------------------------------
         
    async with async_session_factory() as session:
        await crud.add(session, users+posts) # Заполняем БД сразу же всеми моделями
    

async def database_read_users_posts():
    log.info("Getting User's with their Posts's...")
    
    async with async_session_factory() as session:
        users_with_posts = await crud.get_users_with_posts(session)
    
    for user in users_with_posts:
        log.info("User: %s", user)
        log.info('Posts:')
        if not user.posts:
            log.info("No posts")
        
        for post in user.posts:
            log.info('# %s',post)            
        log.info("-------------------------------")
    
    
async def main():
    
    await database_fill() # Вытащить из API данные, отфильтровать нужные, записать в БД
    
    await database_read_users_posts() # Вывести каждого User и все его User.posts
            
                
            

if __name__ == "__main__":
    asyncio.run(main())