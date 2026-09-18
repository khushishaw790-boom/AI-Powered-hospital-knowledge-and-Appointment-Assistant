from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "patient"


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None


@router.get(
    "/",
    tags=["Users"],
    summary="Get all users"
)
def get_users():
    return {
        "users": [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@hospital.com",
                "role": "admin"
            }
        ]
    }


@router.get(
    "/{user_id}",
    tags=["Users"],
    summary="Get user by ID"
)
def get_user(user_id: int):
    return {
        "id": user_id,
        "username": "admin",
        "email": "admin@hospital.com",
        "role": "admin"
    }


@router.post(
    "/",
    tags=["Users"],
    summary="Create user"
)
def create_user(user: UserCreate):
    return {
        "message": "User created successfully",
        "user": user.model_dump()
    }


@router.put(
    "/{user_id}",
    tags=["Users"],
    summary="Update user"
)
def update_user(user_id: int, user: UserUpdate):
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "user": user.model_dump(exclude_none=True)
    }


@router.delete(
    "/{user_id}",
    tags=["Users"],
    summary="Delete user"
)
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }