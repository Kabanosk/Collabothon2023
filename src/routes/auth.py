from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from src.validation import valid_email, valid_password
from src.database import User

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
def register_user(request: Request, username: str = Form(""), password: str = Form("")):
    new_user = User.get()

    if not valid_email(username):
        return {"message": "Email not valid."}
    if not valid_password(password):
        return {"message": "Password not valid."}

    if new_user.exists():
        return {"message": "User exists."}

    new_user = User(-1, login, username, password, 0)
    new_user.add_to_db()
    new_user = User.get(login=new_user.login)
    request.session["user"] = new_user.to_dict()
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login_user(request: Request, username: str = Form(""), password: str = Form("")):
    user = User.get( username)
    if not user:
        return {"message": "User not found."}

    ph = PasswordHasher()
    h_pass = user.password

    try:
        ph.verify(h_pass, password)
    except VerifyMismatchError:
        return {"message": "Bad password"}

    request.session["user"] = user.to_dict()
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/logout")
def logout(request: Request):
    request.session.pop("user")
    return RedirectResponse("/login")
