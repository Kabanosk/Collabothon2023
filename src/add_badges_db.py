#!/usr/bin/env python

from database.utils import pool, add_badge_to_db
from pathlib import Path

def short(path,n):
    return Path(*Path(path).parts[-n:])

p = Path('../static/img/badges/') 

with pool.connect() as conn:
    print('connection success')
    for file in [x for x in p.iterdir() if not x.is_dir()]:
        description = file.stem
        #print(file,data,description)
        print(f'Adding {description}')
        print(f'resolved {short(file.resolve(),4)}')
        #add_badge_to_db(data,description)

