from functools import wraps

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Every function using this decorator
# must accept fastapi.Request as 1st argument
def auth_required(f):
    @wraps(f)
    def check_session(*args, **kwargs):
        request = args[0]
        if not request.session.get("user"):
            return templates.TemplateResponse(
                "login.html", {"error": "Not Authenticated"}
            )
        f(*args, **kwargs)

    return check_session


@router.get("/")
def profile(request: Request):
    return templates.TemplateResponse("profile/main.html", {"request": request})


@router.get("/stats")
def profile_stats(request: Request):
    return templates.TemplateResponse("profile/stats.html", {"request": request})


@router.get("/badges")
def profile_badges(request: Request):
    return templates.TemplateResponse("profile/badges.html", {"request": request})
