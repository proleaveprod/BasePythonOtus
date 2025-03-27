from clickhouse import ClickHouseManager


# Инициализация
manager = ClickHouseManager(
    host='l01-dev-slm.sl.netlo',
    password='1p2a3s4s5',
    db_name='default',
    cache_ttl=1800  # 30 минут
)


# Получаем список БД
dbs = manager.get_databases()
print(f"Available databases: {dbs}")

quit()
# Выбираем конкретную БД
manager.switch_database("analytics")

# Получаем список таблиц
tables = manager.get_tables()
print(f"Tables in analytics: {tables[:5]}...")

# Получаем структуру таблицы
columns = manager.get_columns("Table_114b5d05")
print(f"Columns: {columns}")

# Делаем запрос с фильтрацией
data = manager.get_filtered_data(
    table_name="Table_114b5d05",
    columns=["id", "name", "value"],
    filters={"status": "active", "category": 42},
    limit=10
)
print(f"First row: {data[0] if data else None}")

# Очищаем кеш при необходимости
manager.clear_cache("query")