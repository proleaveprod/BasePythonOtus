import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates') # Общий объект-шаблонизатор

