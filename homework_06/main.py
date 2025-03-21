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
from fetch_api import get_users_posts_data
from models import Base, async_engine, async_session_factory
from models.crud import create_user
from models import User

from logger import logger as log

# Лень делать миграции для такого ДЗ. Удаляю и создаю заново БД, если требуется
async def create_database():
    log.info("Drop and Create of database...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    log.info("Drop and Create of database completed")


async def main():
    # await create_database()    


    # Извлекаем users и posts из API
    # api_data = await get_users_posts_data(timeout = 0.9) 
    
    userdata = {'id': 1, 'firstName': 'Emily', 'lastName': 'Johnson', 'maidenName': 'Smith', 'age': 28, 'gender': 'female', 'email': 'emily.johnson@x.dummyjson.com', 'phone': '+81 965-431-3024', 'username': 'emilys', 'password': 'emilyspass', 'birthDate': '1996-5-30', 'image': 'https://dummyjson.com/icon/emilys/128', 'bloodGroup': 'O-', 'height': 193.24, 'weight': 63.16, 'eyeColor': 'Green', 'hair': {'color': 'Brown', 'type': 'Curly'}, 'ip': '42.48.100.32', 'address': {'address': '626 Main Street', 'city': 'Phoenix', 'state': 'Mississippi', 'stateCode': 'MS', 'postalCode': '29112', 'coordinates': {'lat': -77.16213, 'lng': -92.084824}, 'country': 'United States'}, 'macAddress': '47:fa:41:18:ec:eb', 'university': 'University of Wisconsin--Madison', 'bank': {'cardExpire': '03/26', 'cardNumber': '9289760655481815', 'cardType': 'Elo', 'currency': 'CNY', 'iban': 'YPUXISOBI7TTHPK2BR3HAIXL'}, 'company': {'department': 'Engineering', 'name': 'Dooley, Kozey and Cronin', 'title': 'Sales Manager', 'address': {'address': '263 Tenth Street', 'city': 'San Francisco', 'state': 'Wisconsin', 'stateCode': 'WI', 'postalCode': '37657', 'coordinates': {'lat': 71.814525, 'lng': -161.150263}, 'country': 'United States'}}, 'ein': '977-175', 'ssn': '900-590-289', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36', 'crypto': {'coin': 'Bitcoin', 'wallet': '0xb9fc2fe63b2a6c003f1c324c3bfa53259162181a', 'network': 'Ethereum (ERC20)'}, 'role': 'admin'}
    
    model_fields = {column.name for column in User.__table__.columns}
    filtered_data = {key: value for key, value in userdata.items() if key in model_fields}
    
    user = User(**filtered_data)

    print(user)    
    
    quit()
    async with async_session_factory() as session:
        await create_user(session, userdata)
    
    # users_datalist = data['USERS']['users']
    # posts_datalist = data['POSTS']['posts']
    
    # for user_data in users_datalist:
    #     print(user_data)
    #     print('\n')
    
    
    
            

if __name__ == "__main__":
    asyncio.run(main())