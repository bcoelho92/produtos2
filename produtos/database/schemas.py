from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, EmailStr, Extra
from pydantic.generics import GenericModel
from typing import List

T = TypeVar('T')

class UserSchema(BaseModel):
    name_user: str | None = None
    email: EmailStr  = None

class UserSchemaM(BaseModel):
    name_user: str | None = None

class UserListOutput(BaseModel):
    id_user: int
    name_user: str
    email: str 
    
    class Config:
        orm_mode = True
        extra = Extra.ignore

class ProductsSchema(BaseModel):
    title: str = None
    marca: str = None
    description: Optional[str] | None = None
    
    class Config:
        orm_mode = True
        extra = Extra.ignore

class ProductListOutput(BaseModel):
    id_product: int
    title: str
    marca: str
    description: str
    
    class Config:
        orm_mode = True
    
class FavoritesSchema(BaseModel):
    id_user: int
    id_product: int

class FavoriteSchema(BaseModel):
    id_product: int

class FavoritesstOutput(BaseModel):
    id_favorite: int
    id_user: int
    id_product: int
    class Config:
        orm_mode = True

class ErrorOutput(BaseModel):
    detail: str

class StandardOutput(BaseModel):
    message: str



