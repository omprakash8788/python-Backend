from sqlalchemy.orm import Session
from models import User

from email_validator import(
   validate_email,
   EmailNotValidError

)

from operations import pwd_context

def authenticate_user(
        session:Session,
        username_or_email:str,
        password:str,
) -> User | None:
    try:
        validate_email(username_or_email)
        query_filter = User.email
    except EmailNotValidError:
        query_filter = User.username
    user=(
        session.query(User).filter(query_filter==username_or_email).first()
    )
    if not user or not pwd_context.verify(
        password, user.hashed_password
    ):
        return
    return user


# 107 

SECRET_KEY = "a_very_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

from jose import jwt
from datetime import datetime, timedelta

def create_access_token(data:dict) -> str:
    to_encode=data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt






