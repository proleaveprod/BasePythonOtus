import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, Response

import os

app = FastAPI()

@app.get("/ping/")
async def main():
    return {'message':'pong'}

if __name__ == "__main__":
    uvicorn.run(app='app:app', host='localhost', port=8000)