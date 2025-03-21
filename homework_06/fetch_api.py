import asyncio
import aiohttp
from config.urls import USERS_DATA_URL, POSTS_DATA_URL
from logger import logger as log


async def async_get_api_json(url: str) -> dict:
    """Ассинхронное получение json данных с API-сервиса 

    Args:
        url (str): URL API-сервиса

    Returns:
        dict: Извлеченные данные сервисов API
    """
    log.info('Fetch data from %s ...', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as responce:
            log.info('Fetched data from %s', url)
            return await responce.json()

async def get_users_posts_data(timeout: float = 1.0) -> dict:
    """Ассихронно получить данные USERS и POSTS со всех необходимых API-сервисов 

    Args:
        timeout (float, optional): Макс. время на получение данных со всех сервисов. Defaults to 1.0.

    Returns:
        dict: Словарь с ключами USERS и POST
    """
        
    log.info("Getting data from the Author and Post API's...")
    
    try:
        async with asyncio.timeout(timeout):
            async with asyncio.TaskGroup() as tg:
                task_users = tg.create_task(async_get_api_json(USERS_DATA_URL))
                task_posts = tg.create_task(async_get_api_json(POSTS_DATA_URL))
    except TimeoutError:
        log.error("Timeout error")
        return None
    
    users = task_users.result().get('users')
    posts = task_posts.result().get('posts')
    
    if users and posts:
        log.info("Data from Author and Post received")
        return {'users': users, 'posts': posts}
    else:
        log.error("Can't fetch whole data")
        return None 
        
    

    