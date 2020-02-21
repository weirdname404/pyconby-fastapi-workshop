from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import engine
from .deps import get_db
from .api import items, users

app = FastAPI()


@app.get('/')
def read_root():
    return {"msg": "sanity check"}


@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)


app.include_router(users.router, tags=['users'])
app.include_router(items.router, tags=['items'])
