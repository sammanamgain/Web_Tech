from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def passwordhash(password:str):
         hashedPassword=pwd_cxt.hash(password)  
         return hashedPassword
     
     
class verify():
    def verifyhash(plain_password,hashed_password):
        return pwd_cxt.verify(plain_password,hashed_password)