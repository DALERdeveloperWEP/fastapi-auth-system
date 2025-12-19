from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.dependencies import get_db
from app.models.authtoken import AuthToken
from app.schemas.users import UserResponse

router = APIRouter(prefix='/api/users', tags=['Users'])


token_schema = HTTPBearer()

@router.get('/profile', response_model=UserResponse)
def get_profile(token: Annotated[HTTPAuthorizationCredentials, Depends(token_schema)], db: Annotated[Session, Depends(get_db)]):
    exists_token = db.query(AuthToken).filter(AuthToken.token==token.credentials).first()
    if not exists_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    user = exists_token.user
    return user