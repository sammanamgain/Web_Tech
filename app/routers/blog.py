import statistics
from typing import Annotated, List
from fastapi import Depends , APIRouter, HTTPException, Response,status
import models

import models, pydenticschema, routers
from sqlalchemy.orm import Session
# from database import SessionLocal
import database
from database import SessionLocal
import oauth2

router=APIRouter()

@router.get("/blog/get", response_model=List[pydenticschema.showBlog], tags=["blogs"])
def getdata(db: database.SessionLocal = Depends(database.get_db), get_current_user:pydenticschema.User=Depends(oauth2.get_current_user)):
    new_blog = db.query(models.Blog).all()

    return new_blog



@router.post("/blog/add", tags=["blogs"])
# depends keyword is used to inject dependency ,which will return value from get_db to adddata
def adddata(request: pydenticschema.Blog, db: Session = Depends(database.get_db)):
    # models.Blog is the class that we made in models.py in which we are passing the arguments
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)  # adding the data to the database , or object is mapped to db
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.get("/blog/get/{id}", status_code=200, response_model=pydenticschema.showBlog, tags=["blogs"])
def getdata(id: int, db: Session = Depends(database.get_db)):
    # if we use all , we need to define list of reponse_model
    new_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not new_blog:
        raise HTTPException(
            status_code=statistics.HTTP_404_NOT_FOUND, detail="not found in server")
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details":" blog with this id not found"}
    return new_blog


@router.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete(id: int, db: Session = Depends(database.get_db)):
    b = db.query(models.Blog).filter(models.Blog.id ==
                                     id)
    if not b.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
    b.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/blog/update/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id: int, request: pydenticschema.Blog, db: Session = Depends(database.get_db)):

    b = db.query(models.Blog).filter(models.Blog.id == id)
    if not b.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
    b.update(
        {"title": request.title, "body": request.body})
    db.commit()
    return {"sucessfully update"}
