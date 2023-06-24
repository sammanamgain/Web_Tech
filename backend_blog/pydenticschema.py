from pydantic import BaseModel


class Blog(BaseModel):
    Name: str
    Age: int
