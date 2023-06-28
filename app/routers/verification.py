from datetime import timedelta
import statistics
import tokens,routers
from typing import List
from fastapi import Depends , APIRouter, HTTPException, Response,status
from routers import user
from tokens import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
import models, pydenticschema, routers
from sqlalchemy.orm import Session
# from database import SessionLocal
import database
from database import SessionLocal
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router=APIRouter()

import hashing
@router.post("/user/login",  tags=["login"])
def verify(request: OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    new_blog = db.query(models.User).filter(models.User.email == request.username).first()
    if not new_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="you made a mistake , plz review it")
    if not hashing.verify.verifyhash(request.password,new_blog.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="you entered a wrong password , plz review it")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokens.create_access_token(data={"sub": new_blog.email}, )
    return {"access_token": access_token, "token_type": "bearer"}