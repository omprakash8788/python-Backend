
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database import Base, User
from db_connection import get_engine, get_session
from operations import add_user

# Import your Pydantic schemas
from schemas import (
    UserCreateBody,
    UserCreateResponse,
    ResponseCreateUser,
)



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=get_engine())
    yield



app = FastAPI(
    title="Saas application",
    lifespan=lifespan,
)


@app.post(
    "/register/user",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseCreateUser,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "The user already exists"
        }
    },
)
def register(
    user: UserCreateBody,
    session: Session = Depends(get_session),
) -> ResponseCreateUser:

    created_user = add_user(
        session=session,
        **user.model_dump(),
    )

    if created_user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists",
        )

    user_response = UserCreateResponse(
        username=created_user.username,
        email=created_user.email,
    )

    return ResponseCreateUser(
        message="User created",
        user=user_response,
    )

