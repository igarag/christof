import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import camera

app = FastAPI()

app.include_router(camera.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
