from pathlib import Path
from configparser import ConfigParser
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent

# -------------------------[DATABASE]-------------------------
auth_config = ConfigParser()
auth_config.read(BASE_DIR / 'auth.ini') 

db_user = auth_config['auth']['username'] 
db_password = auth_config['auth']['password'] 
db_name = auth_config['auth']['db_name']

db_url = f"postgresql+psycopg://{db_user}:{db_password}@localhost:5432/{db_name}"
db_echo = True

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# ------------------------[TEMPLATING]------------------------
templates = Jinja2Templates(directory='templates') # Общий объект-шаблонизатор