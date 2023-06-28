# this is about the creating object for the post request method
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True
# to define the schema for response body
# as it is used to filter the response body which is originally contains in database so orm is needed
# so class config and orm mode is set true




class User(BaseModel):
    name:str
    email:str
    password:str
    
    
class showuser(BaseModel):
    name:str
    email:str
    blogs:list[Blog]
    class Config():
        orm_mode = True
        
        
class auth(BaseModel):
    email:str
    password:str
   


class showBlog(BaseModel):
    title:str
    body:str
    creator:showuser
    # title:str  # here if we didnot mention title, it will only show attributes of blog class but need to use Blog instead of Basemodel
    # body:str
    class Config():
        orm_mode = True
        
        
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str