from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
from sqlmodel import select
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from db.db import get_db
from db.models import UserAccount, Attendance, UserBase


class UserDetail(UserBase):
    id: int
    attendances: List[Attendance]


class CheckUserResponse(BaseModel):
    exists: bool
    user: Optional[UserDetail]


class UserListResponse(BaseModel):
    skip: int
    limit: int
    count: int
    users: List[UserAccount]




users_router = APIRouter()


@users_router.get(
    '/check',
    response_model=CheckUserResponse,
    name='Проверка',
    description='Проверка, состоит ли пользователь в проекте "Московское долголетие"'
)
def check(fullname: str, birthday: date, db: Session = Depends(get_db)):
    user = db.query(UserAccount).filter_by(birthday=birthday, fullname=fullname).first()
    return {
        'exists': True if user else False,
        'user': user
    }


@users_router.get(
    '/users/{id}',
    response_model=UserDetail,
    name='Пользователь',
    description='Получение пользователя по id',
)
def get_user(id: int, db: Session = Depends(get_db)):
    # TODO: 404 exception
    user = db.query(UserAccount).get(id)
    return user


@users_router.get(
    '/users',
    response_model=UserListResponse,
    name='Пользователи',
    description='Получение пользователей'
)
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserAccount).limit(limit).offset(skip).all()
    count = len(users)
    return {
        'skip': skip,
        'limit': limit,
        'count': count,
        'users': users
    }



