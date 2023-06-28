
import tokens

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pydenticschema

from typing import Annotated

from fastapi import Depends, HTTPException,status
from jose import JWTError

#from backend_blog.pydenticschema import TokenData
#from login route , fastapi will fetch the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def get_current_user(data: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    #decoding the token 
    return tokens.verifytoken(data,credentials_exception)