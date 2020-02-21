from pydantic import BaseModel, Field
from typing import List


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str = Field(..., max_length=30)


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
