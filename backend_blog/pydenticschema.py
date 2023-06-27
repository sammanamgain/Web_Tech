# this is about the creating object for the post request method
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body : str

#to define the schema for response body  
#as it is used to filter the response body which is originally contains in database so orm is needed
# so class config and orm mode is set true
class showBlog(Blog):
    title:str # here if we didnot mention title, it will only show attributes of blog class
    class Config():
        orm_mode = True