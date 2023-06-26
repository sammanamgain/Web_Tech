from fastapi import Depends, FastAPI
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


@app.get("/blogs")
async def root(limit=10):
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
#this is used to create the instance of database session which is db object , yield is generator here
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog/add")
def adddata(request: pydenticschema.Blog, db: Session = Depends(get_db)): #depends keyword is used to inject dependency ,which will return value from get_db to adddata
    new_blog = models.Blog(title=request.title, body=request.body) #models.Blog is the class that we made in models.py in which we are passing the arguments
    db.add(new_blog) #adding the data to the database , or object is mapped to db
    db.commit()
    db.refresh(new_blog)
    return new_blog
