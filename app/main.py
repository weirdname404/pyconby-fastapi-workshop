from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import SessionLocal, engine

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {"msg": "sanity check"}


@app.get('/users/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)
