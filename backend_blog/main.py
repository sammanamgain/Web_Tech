from fastapi import FastAPI
import pydenticschema
from models import User
from database import Base, engine, SessionLocal

# running the server or app , main app will start from this code , this is the main file 
app = FastAPI()

# this is defining the routing , this the path that client uses to access the file , which contains get method 
@app.get("/")
# this is the function that will be executed when the client uses the path
async def root():
    return {"message": "Hello World"}

#another path
@app.get("/samman")
async def root():
    return {"Name": "samman"}

#we can also mention query parameters
# query parameters
@app.get("/blogs")
async def root(limit=10):
    return {"blogpost": f' {limit} blogs from the database'}

# in the path you can use variables too like i have used id here , i can 1 2 3 or any things inplace of id , but only integer as i mentioned its type strictly
@app.get("/blogs/{id}")
async def root(id: int):
    return {"blogpost": id}


# using post request to create a blog
#why r we using post method , because we are creating a blog , we are not getting any data from the server , we are sending data to the server
# to send data to server , we alaways need to use pydantic schema , to define the structure of the data
#and to perform validation in the forms too
@app.post("/blog/add")
def adddata(request: pydenticschema.Blog):
    return {f'this is the blog having title {request.Name}'}

#this is the code that binds the database with the  app and updates the all the tables that we made in database and models.py
Base.metadata.create_all(bind=engine)
