#!/usr/bin/env python

from pathlib import Path

from database.utils import add_badge_to_db, pool


def short(path, n):
    return Path(*Path(path).parts[-n:])


p = Path("../static/img/badges/")

with pool.connect() as conn:
    print("connection success")
    for file in [x for x in p.iterdir() if not x.is_dir()]:
        description = file.stem
        path = "/" + str(short(file.resolve(), 4))
        print(f"Adding {description}")
        print(f"resolved {path}")
        add_badge_to_db(path, description)
