from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from src.validation import valid_email, valid_password
from src.database.utils import get_user_by_username, add_user

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
def register_user(request: Request, email: str = Form(""), username: str = Form(""), password: str = Form("")):
    new_user = get_user_by_username(username)

    if not valid_email(username):
        return templates.TemplateResponse('login.html', {'request': request, 'message': 'Email not valid'})
    if not valid_password(password):
        return templates.TemplateResponse('login.html', {
            'request': request,
            'message': 'Password must contains at least 8 characters, one letter, one number '
                       'and one special character from "@$!%*#?&"'
        })

    if new_user:
        return templates.TemplateResponse('login.html', {'request': request, 'message': 'User exists'})

    ph = PasswordHasher()
    h_pass = ph.hash(password)
    add_user(username, email, h_pass)
    new_user = get_user_by_username(username)

    request.session["user"] = {
        'id': new_user[0],
        'username': new_user[1],
        'email': new_user[2],
        'password': new_user[3],
        'inventory': new_user[4]
    }
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login_user(request: Request, username: str = Form(""), password: str = Form("")):
    user = get_user_by_username(username)
    if not user:
        return templates.TemplateResponse('login.html', {'request': request, 'message': 'User not found'})

    ph = PasswordHasher()
    h_pass = user.password

    try:
        ph.verify(h_pass, password)
    except VerifyMismatchError:
        return templates.TemplateResponse('login.html', {'request': request, 'message': 'Bad password'})

    request.session["user"] = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'password': user[3],
        'inventory': user[4]
    }
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/logout")
def logout(request: Request):
    request.session.pop("user")
    return RedirectResponse("/login")
