import numpy as np
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database.utils import add_user, data_for_model, get_user_by_username

# from model import get_model
from validation import valid_email, valid_password

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/register", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register", response_class=HTMLResponse)
def register_user(
    request: Request,
    email: str = Form(""),
    username: str = Form(""),
    password: str = Form(""),
):
    new_user = get_user_by_username(username)

    if not valid_email(email):
        return templates.TemplateResponse(
            "register.html", {"request": request, "message": "Email not valid"}
        )
    if not valid_password(password):
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "message": "Password must contains at least 8 characters, one letter, one number "
                'and one special character from "@$!%*#?&"',
            },
        )

    if new_user:
        return templates.TemplateResponse(
            "register.html", {"request": request, "message": "User exists"}
        )

    ph = PasswordHasher()
    h_pass = ph.hash(password)
    add_user(username, email, h_pass, 0)
    new_user = get_user_by_username(username)

    # model = request.session.get("model")
    # n = model.data.shape[1]
    # if model:
    #     request.state.model = model.add_user(np.zeros((n,)))
    # else:
    #     request.state.model = get_model(data_for_model())

    request.state.user = {
        "id": new_user[0],
        "username": new_user[1],
        "email": new_user[2],
        "password": new_user[3],
        # 'inventory': new_user[4]
    }
    return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login", response_class=HTMLResponse)
def login_user(request: Request, username: str = Form(""), password: str = Form("")):
    user = get_user_by_username(username)
    if not user:
        return templates.TemplateResponse(
            "login.html", {"request": request, "message": "User not found"}
        )

    ph = PasswordHasher()
    h_pass = user.password

    try:
        ph.verify(h_pass, password)
    except VerifyMismatchError:
        return templates.TemplateResponse(
            "login.html", {"request": request, "message": "Bad password"}
        )

    request.state.user = {
        "id": user[0],
        "username": user[1],
        "email": user[2],
        "password": user[3],
        # 'inventory': user[4]
    }
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/logout")
def logout(request: Request):
    request.session.pop("user")
    return RedirectResponse("/login")
