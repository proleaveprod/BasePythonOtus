from clickhouse import ClickHouseManager
from clickhouse_driver import Client

# Инициализация
manager = ClickHouseManager(host='l01-dev-slm.sl.netlo', password='1p2a3s4s5')

# Получаем список БД
# dbs = manager.get_databases()
# print(f"Available databases: {dbs}")

# Выбираем конкретную БД
manager.switch_database("SLM_Stat")

# Получаем список таблиц
# tables = manager.get_tables()
# print(f"Tables in SLM_Stat: {tables[:5]}...")

# Получаем структуру таблицы
# columns = manager.get_columns("Common")


data = manager.get_filtered_data(
    table_name="Devices",
    columns=["identifier", "devID", "shortName"],
    filters={"canVersion": "5.0.0"},
    limit=2
)

data = manager.query("SELECT 1+2")[0][0]
print(data)

# # Очищаем кеш при необходимости
# manager.clear_cache("query")