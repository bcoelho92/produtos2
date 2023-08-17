from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from typing import List

T = TypeVar('T')

class UserSchema(BaseModel):
    name_user: Optional[str] = None
    email: str = None

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class UserListOutput(BaseModel):
    id_user: int
    name_user: str
    email: str
    
    class Config:
        orm_mode = True

class RequestIdUser(BaseModel):
    id_user: int = None 

class ProductsSchema(BaseModel):
    title: str = None
    marca: str = None
    description: str = None

class RequestProducts(BaseModel):
    parameter: ProductsSchema = Field(...)

class RequestIdProducts(BaseModel):
    id_product: int = None 

class ErrorOutput(BaseModel):
    detail: str

class StandardOutput(BaseModel):
    message: str
