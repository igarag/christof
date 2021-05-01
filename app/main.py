from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import camera

app = FastAPI()

app.include_router(camera.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.route('/')
def index(request: Request) -> HTMLResponse:
    return templates.TemplatesResponse('index.html', {'request': request})
