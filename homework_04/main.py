import uvicorn
from modules.common import *
from modules.routers.api import router as api_router
from modules.routers.view import router as view_router

app = FastAPI(title="ПЕРСОНАЖИ ИЗ КОМИКСОВ", description="Вау прикольный сайт с персонажами из комиксов")
app.include_router(view_router)  
app.include_router(api_router)  

# Кастомный обработчик 404 - Not Found
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: Exception):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True,  host='127.0.0.1', port=8000) 