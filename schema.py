from pydantic import BaseModel,EmailStr

class accountcreate(BaseModel):
    name:str
    email:EmailStr
    age:int
    city:str
    balance:float

class accountupdate(BaseModel):
    name:str = None
    email:EmailStr = None
    age:int = None
    city:str = None

class accountout(BaseModel):
    id:int
    name:str
    email:EmailStr
    age:int
    city:str
    balance:float

    class Config:
        from_attributes=True

class transaction(BaseModel):
    amount:float

class transactionout(BaseModel):
    id:int
    amount:float
    type:str
    account_id:int

    class Config:
        from_attributes=True

    