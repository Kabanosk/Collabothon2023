import numpy as np
from fastapi import APIRouter, Request, Form, File, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from model import Model
from database.utils import add_plant_to_inventory, add_photo, get_plant_by_name

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.post('/add')
def add_to_inventory(
        request: Request,
        name: str = Form(""),
        photo: bytes = File(),
        age: float = Form(0),
):
    user_id = request.session.get("user")['id']
    # photo_id = add_photo(photo)
    photo_id = 0
    plant = get_plant_by_name(name)
    if not plant:
        return templates.TemplateResponse('profile/profile.html',
                                          {"request": request, "message": "Bad plant name"})
    add_plant_to_inventory(user_id, plant[0], photo_id, age=age)
    model = Model.load()
    if user_id in model.data:
        model.data[user_id][0] += 1
    else:
        n = len(model.data[list(model.data.keys())[0]])
        model.data[user_id] = np.zeros((n,))
        model.data[user_id][0] = 1

    model.train()
    model.save()
    return RedirectResponse('/', status_code=status.HTTP_303_SEE_OTHER)
