from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def passwordhash(password:str):
         hashedPassword=pwd_cxt.hash(password)  
         return hashedPassword