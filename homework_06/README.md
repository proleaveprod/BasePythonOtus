# Домашнее задание "Асинхронная работа с сетью и БД"

### Запуск PostgreSQL-контейнера

Выполняется с помощью docker-команды:
```
docker run --name postgres_homework06 -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=postgres -d postgres
```

### Данные для авторизации

Хранятся в auth.ini. В реалиях auth.ini должен быть добавлен в .gitignore файл. Оставил просто для наглядности 

