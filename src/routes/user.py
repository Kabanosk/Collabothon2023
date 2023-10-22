from functools import wraps

import numpy as np
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from database.utils import get_all_plants_from_db
from model import Model

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
    model = Model.load()
    user = request.session.get("user")
    if not user:
        return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)

    user_vec = model.data[user['id']]
    recommended_users = model.get_recommended_users(user_vec.reshape((1, -1)))
    keys = [list(model.data.keys())[i] for i in sorted(recommended_users[0])]
    ids = [np.nonzero(model.data[u])[0] for u in keys]

    recommended_plants_id = set(np.concatenate(ids)).difference(set(list(np.nonzero(user_vec)[0])))
    plants = np.array(get_all_plants_from_db())
    plants_d = {}
    for arr in plants:
        plants_d[arr[0]] = arr

    recommended_plants = [plants_d[x] for x in recommended_plants_id]

    return templates.TemplateResponse(
        "profile/main.html",
        {"request": request, "recommended_plants": recommended_plants},
    )


@router.get("/stats")
def profile_stats(request: Request):
    return templates.TemplateResponse("profile/stats.html", {"request": request})


@router.get("/badges")
def profile_badges(request: Request):
    return templates.TemplateResponse("profile/badges.html", {"request": request})
