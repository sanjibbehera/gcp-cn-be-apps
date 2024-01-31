from pydantic import BaseModel

class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    user_name:str
    password:str        

class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:str 
    user_name:str  
    class Config():
        orm_mode=True       

class Login(BaseModel):
    username:   str
    password:   str    
    class Config():
        orm_mode=True  