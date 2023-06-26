# this is about the creating object for the post request method
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body : str
