from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

class ProductCreate(BaseModel):
    name:str
    description:str
    price:float
    category:str