from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response, status
import models
from models import Blog
import pydenticschema

from pydenticschema import Blog

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


# running the server or app , main app will start from this code , this is the main file
app = FastAPI()

# this is defining the routing , this the path that client uses to access the file , which contains get method


@app.get("/")
# this is the function that will be executed when the client uses the path
async def root():
    return {"message": "Hello World"}

# another path


@app.get("/samman")
async def root():
    return {"Name": "samman"}

# we can also mention query parameters
# query parameters


@app.get("/blogs", status_code=status.HTTP_200_OK)
async def root(limit=10,):
    return {"blogpost": f' {limit} blogs from the database'}

# in the path you can use variables too like i have used id here , i can 1 2 3 or any things inplace of id , but only integer as i mentioned its type strictly


@app.get("/blogs/{id}")
async def root(id: int):
    return {"blogpost": id}


# using post request to create a blog
# why r we using post method , because we are creating a blog , we are not getting any data from the server , we are sending data to the server
# to send data to server , we alaways need to use pydantic schema , to define the structure of the data
# and to perform validation in the forms too


# this is the code that binds the database with the  app and updates the all the tables that we made in database and models.py
Base.metadata.create_all(bind=engine)

models.Base.metadata.create_all(bind=engine)
# this is used to create the instance of database session which is db object , yield is generator here


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# retriving the blog from database
# we are defining reponse body as list as it return the multiple blog not a single
#and we need to define the schema for each blog, so we are using list here
@app.get("/blog/get",response_model=List[pydenticschema.showBlog])
def getdata(db: Session = Depends(get_db)):
    new_blog = db.query(models.Blog).all()

    return new_blog


@app.post("/blog/add")
# depends keyword is used to inject dependency ,which will return value from get_db to adddata
def adddata(request: pydenticschema.Blog, db: Session = Depends(get_db)):
    # models.Blog is the class that we made in models.py in which we are passing the arguments
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)  # adding the data to the database , or object is mapped to db
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog/get/{id}", status_code=200,response_model=pydenticschema.showBlog)
def getdata(id: int, db: Session = Depends(get_db)):
    new_blog = db.query(models.Blog).filter(models.Blog.id == id).first() # if we use all , we need to define list of reponse_model
    if not new_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details":" blog with this id not found"}
    return new_blog


@app.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id ==
                                     id)
    if not b.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
    b.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/blog/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: pydenticschema.Blog, db: Session = Depends(get_db)):

    b = db.query(models.Blog).filter(models.Blog.id == id)
    if not b.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found in server")
    b.update(
        {"title": request.title, "body": request.body})
    db.commit()
    return {"sucessfully update"}
