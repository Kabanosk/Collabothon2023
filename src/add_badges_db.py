#!/usr/bin/env python

from pathlib import Path

from database.utils import add_badge_to_db, pool

p = Path("../static/img/badges")

with pool.connect() as conn:
    print("connection success")
    for file in [x for x in p.iterdir() is not p.is_dir()]:
        data = file.read_bytes()
        description = file.stem
        add_badge_to_db(data, description)
