
# this file is all about of creating the database file and connnecting to the db using engine and creating
# session to  perform crud operation and creating base class to create table in database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///C:/Users/amgai/OneDrive/Desktop/Web_Tech/app/data.db'


# this section is connecting the database using engine
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# database is connected with some args




engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# to perform crud operation we need session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# to create table in database we need to create a base class ,which is called orm , which is creating object and mapping to the models
Base = declarative_base()





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

