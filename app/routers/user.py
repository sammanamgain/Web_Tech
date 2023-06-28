import statistics
from typing import List
from fastapi import Depends , APIRouter, HTTPException, Response,status
import models, pydenticschema, routers
from sqlalchemy.orm import Session
# from database import SessionLocal
import database
from database import SessionLocal
import hashing
router=APIRouter()



@router.post("/add/user", tags=["users"])
def create_user(request: pydenticschema.User, db: Session = Depends(database.get_db)):

    new_blog = models.User(
        name=request.name, email=request.email, password=hashing.Hash.passwordhash(request.password))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/user/get/{id}", status_code=200, response_model=pydenticschema.showuser, tags=["users"])
def geuser(id: int, db: Session = Depends(database.get_db)):
    # if we use all , we need to define list of reponse_model
    new_blog = db.query(models.User).filter(models.User.id == id).first()
    if not new_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details":" blog with this id not found"}
    return new_blog
