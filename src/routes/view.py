from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get('/')
def profile(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
