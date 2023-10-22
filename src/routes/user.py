from functools import wraps

import numpy as np
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from database.utils import get_all_plants_from_db, get_user_badge, get_user_by_username, get_plant_stats
from model import Model
import matplotlib.pyplot as plt
import mpld3
from datetime import timedelta, date

router = APIRouter()
templates = Jinja2Templates(directory="templates/profile")


@router.get("/")
def profile(request: Request):
    model = Model.load()
    user = request.session.get("user")
    if not user:
        return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)

    recommended_plants = None
    if user['id'] in model.data:
        user_vec = model.data[user['id']]
        recommended_users = model.get_recommended_users(
            user_vec.reshape((1, -1)))
        keys = [list(model.data.keys())[i]
                for i in sorted(recommended_users[0])]
        ids = [np.nonzero(model.data[u])[0] for u in keys]

        recommended_plants_id = set(np.concatenate(ids)).difference(
            set(list(np.nonzero(user_vec)[0])))
        plants = np.array(get_all_plants_from_db())
        plants_d = {}
        for arr in plants:
            plants_d[arr[0]] = arr

        recommended_plants = [plants_d[x] for x in recommended_plants_id]

    user_badges = get_user_badge(user['id'])
    return templates.TemplateResponse(
        "profile.html",
        {"request": request, "recommended_plants": recommended_plants,
            "badges": user_badges},
    )


@router.get("/stats")
def profile_stats(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/login', status_code=status.HTTP_303_SEE_OTHER)
    plant_stats = get_plant_stats(user['id'])
    xs = [plant_stats[0].creation_date - timedelta(days=1)]
    ys = [0]
    zs = [0]
    co2_cnt = 0
    o2_cnt = 0
    html_graph = None
    if plant_stats:
        first_elem = plant_stats[0].creation_date
        last_elem = plant_stats[-1].creation_date
        i = 0
        while first_elem <= last_elem:
            while i < len(plant_stats) and plant_stats[i].creation_date.day == first_elem.day:
                co2_cnt += plant_stats[i].co2_absorbtion
                o2_cnt += plant_stats[i].oxygen_emission
                i += 1
            xs.append(first_elem)
            ys.append(co2_cnt + ys[-1])
            zs.append(o2_cnt + zs[-1])
            first_elem += timedelta(days=1)
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots()
        ax1.plot(xs,ys)
        ax2.scatter(xs,zs)
        html_graph1 = mpld3.fig_to_html(fig1)
        html_graph2 = mpld3.fig_to_html(fig2)

    return templates.TemplateResponse("statistics.html", {"request": request, "plot": [html_graph1, html_graph2]})



@router.get("/leaderboard")
def profile_stats(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/login', status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("leaderboard.html", {"request": request})


@router.get("/badges")
def profile_badges(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/login', status_code=status.HTTP_303_SEE_OTHER)
    user_badges = get_user_badge(user['id'])
    return templates.TemplateResponse("badges.html", {"request": request, "badges": user_badges})
