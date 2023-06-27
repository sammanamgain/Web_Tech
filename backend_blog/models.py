# this file is all about the structure of tables of database


from sqlalchemy import Column, Integer, String
# we are importing base to create object and mapping to table
from database import Base


class Blog(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body  = Column(String, unique=True, index=True)


class User(Base):
    __tablename__ = "Logininfo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email  = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    
