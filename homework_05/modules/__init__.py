import sys, os

# Добавляем корневую папку в sys.path, чтобы можно было запускать модули отдельно
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from . import classes, database, common
from .routers import view, api