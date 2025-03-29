from clickhouse_driver import Client
from cachetools import TTLCache
from functools import wraps
import time
from typing import Dict, List, Optional, Union

class ClickHouseManager:
    def __init__(self, host: str, password: str, cache_ttl: int = 3600, max_cache_size: int = 1000):
        self.client = Client(host=host, password=password)
        self.db_name = str()
        
        # Кеши для метаданных
        self._databases_cache = TTLCache(maxsize=1, ttl=cache_ttl)
        self._tables_cache = TTLCache(maxsize=max_cache_size, ttl=cache_ttl)
        self._columns_cache = TTLCache(maxsize=max_cache_size, ttl=cache_ttl)
        
        # Кеш для результатов запросов (ключ - текст запроса + параметры)
        self._query_cache = TTLCache(maxsize=max_cache_size, ttl=cache_ttl//2)

    def _cache_query(func):
        """Декоратор для кеширования результатов методов"""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
            
            if cache_key in self._query_cache:
                return self._query_cache[cache_key]
            
            result = func(self, *args, **kwargs)
            self._query_cache[cache_key] = result
            return result
        return wrapper

    @_cache_query
    def get_databases(self) -> List[str]:
        """Получить список всех доступных БД"""
        if 'databases' in self._databases_cache:
            return self._databases_cache['databases']
        
        databases = [row[0] for row in self.client.execute("SHOW DATABASES")]
        self._databases_cache['databases'] = databases
        return databases

    @_cache_query
    def get_tables(self, db_name: str = None) -> List[str]:
        """Получить список таблиц в указанной БД"""
        db = db_name or self.db_name
        if not db:
            raise ValueError("Database name not specified")
        
        cache_key = f"tables_{db}"
        if cache_key in self._tables_cache:
            return self._tables_cache[cache_key]
        
        tables = [row[0] for row in self.client.execute(f"SHOW TABLES FROM {db}")]
        self._tables_cache[cache_key] = tables
        return tables

    @_cache_query
    def get_columns(self, table_name: str, db_name: str = None) -> Dict[str, str]:
        """Получить структуру таблицы {column_name: type}"""
        db = db_name or self.db_name
        if not db:
            raise ValueError("Database name not specified")
        
        cache_key = f"columns_{db}_{table_name}"
        if cache_key in self._columns_cache:
            return self._columns_cache[cache_key]
        
        columns = {
            row[0]: row[1] 
            for row in self.client.execute(f"DESCRIBE TABLE {db}.{table_name}")
        }
        self._columns_cache[cache_key] = columns
        return columns

    def query(
        self,
        query: str,
        params: dict = None,
        use_cache: bool = False,
        cache_key: str = None
    ) -> List[tuple]:
        """Выполнить произвольный SQL запрос с кешированием"""
        if not use_cache:
            return self.client.execute(query, params=params)
        
        # Формируем ключ кеша
        effective_cache_key = cache_key or f"query_{hash(query)}_{frozenset(params.items()) if params else ''}"
        
        if effective_cache_key in self._query_cache:
            return self._query_cache[effective_cache_key]
        
        result = self.client.execute(query, params=params)
        self._query_cache[effective_cache_key] = result
        return result

    def get_filtered_data(
        self,
        table_name: str,
        columns: Union[str, List[str]] = "*",
        filters: Dict[str, Union[str, int, float]] = None,
        limit: int = 100,
        db_name: str = None,
        use_cache: bool = False
    ) -> List[tuple]:
        """Получить данные из таблицы с фильтрацией"""
        db = db_name or self.db_name
        if not db:
            raise ValueError("Database name not specified")
        
        # Формируем запрос
        cols = ", ".join(columns) if isinstance(columns, list) else columns
        where = ""
        if filters:
            where = "WHERE " + " AND ".join([f"{k} = %({k})s" for k in filters.keys()])
        
        query = f"SELECT {cols} FROM {db}.{table_name} {where} LIMIT {limit}"
        
        # Ключ кеширования
        cache_key = None
        if use_cache:
            cache_key = f"data_{db}_{table_name}_{hash(cols)}_{frozenset(filters.items()) if filters else ''}_{limit}"
        
        return self.query(query, params=filters, use_cache=use_cache, cache_key=cache_key)

    def clear_cache(self, cache_type: str = None):
        """Очистить указанный кеш или все"""
        if cache_type == "databases":
            self._databases_cache.clear()
        elif cache_type == "tables":
            self._tables_cache.clear()
        elif cache_type == "columns":
            self._columns_cache.clear()
        elif cache_type == "query":
            self._query_cache.clear()
        else:
            self._databases_cache.clear()
            self._tables_cache.clear()
            self._columns_cache.clear()
            self._query_cache.clear()

    def switch_database(self, new_db_name: str):
        """Переключиться на другую базу данных"""
        self.client.execute(f"USE {new_db_name}")
        self.db_name = new_db_name
        # Очищаем кеш таблиц при смене БД
        self._tables_cache.clear()