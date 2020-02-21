from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, deps, schemas
from ..deps import get_db

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_item_for_user(db=db, item=item, user_id=user_id)


@router.get('/items/', response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)
