import os
from datetime import datetime
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from sqlalchemy import UniqueConstraint, String, Column




print("sucessfull 1 ")

class User(SQLModel, table=True):

    __tablename__ = "user"

    id: int = Field(primary_key=True)
    name: str
    hashed_password: str
    email: str = Field(sa_column=Column("email", String(40), unique=True))
    role_name: str = Field(default=None, foreign_key="role.name")


   
class Role(SQLModel, table=True):

    __tablename__ = "role"
    id: int = Field(primary_key=True)
    name: str= Field(sa_column=Column("name", String(40), unique=True))


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int = Field(primary_key=True)
    name:str = Field(sa_column=Column("name", String(40), unique=True))
    amount: float
    discription: str

class OrderInfo(SQLModel, table=True):
    __tablename__ = "orderinfo"

    id: int = Field(primary_key=True)
    order_id: str
    product_id: str = Field(default=None, foreign_key="product.name")
    user_email: str = Field(default=None, foreign_key="user.email")





