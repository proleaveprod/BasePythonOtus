DB_URL = "postgresql+psycopg2://username:passwd@localhost:5432/blog"
# DB_URL = "postgresql+pg8000://username:passwd@localhost:5432/blog"
ASYNC_DB_URL = DB_URL.replace("psycopg2", "asyncpg")
DB_ECHO = False
# DB_ECHO = True
DB_POOL_SIZE = 50
DB_POOL_MAX_OVERFLOW = 10