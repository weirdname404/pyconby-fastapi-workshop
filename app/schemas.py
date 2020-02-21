from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(..., max_length=30)


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
