from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///C:/Users/amgai/OneDrive/Desktop/Web_Tech/data.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#database is connected with some args 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#to perform crud operation we need session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# to create table in database we need to create a base class
Base = declarative_base()