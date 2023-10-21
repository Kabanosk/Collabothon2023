from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functools import wraps
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

@router.get('/')
def profile(request: Reqeust):
    return templates.TemplateResponses("home.html",{"request":request})


