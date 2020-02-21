from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id=int):
    return db.query(models.User).filter(models.User.id==user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email==email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hash_pass = f"fake-{user.password}"
    new_user = models.User(email=user.email, hashed_password=hash_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_items(db: Session, item: schemas.ItemCreate, user_id: int):
    item = models.Item(**item.dict(), owner_id=user_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
