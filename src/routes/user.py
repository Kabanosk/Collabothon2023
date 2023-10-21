from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functools import wraps
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


# Every function using this decorator
# must accept fastapi.Request as 1st argument
def auth_required(f):
    @wraps(f)
    def check_session(*args,**kwargs):
        request = args[0]
        if not request.session.get('user')
            return templates.TemplateResponse("login.html",{"error": "Not Authenticated"})
        f(*argc,**kwargs)
    return check_session


@router.get('/profile')
def profile(request: Reqeust):
    return templates.TemplateResponses("profile.html",{"request":request})

@router.get('/profile/stats')
def profile_stats(request: Request):
    return templates.TemplateResponses("profile_stats.html",{"request",request})

@router.get('/profile/badges')
def profile_badges(request: Request):
    return templates.TemplateResponses("profile_badges.html",{"request",request})


