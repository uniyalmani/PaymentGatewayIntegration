from pydantic import BaseModel, validator
from typing import Union
from fastapi import APIRouter, Depends,Header
# from app.utilities.dependencies import get_session
from app.utilities.helpers import hash_password, verify_password, create_jwt_token, is_valid_token
from app.utilities.dependencies import get_decoded_token_data
from app.services import product
from datetime import datetime

router = APIRouter()



class ProductModel(BaseModel):
    name: str
    amount: float
    discription: str

@router.post('/create_product',
        tags=["Admin Routes"],
        description="**Route for creating product**")
def create_product(product_info: ProductModel, 
    product_handler: object = Depends(product.ProductHandler),
    token: Union[str, None] = Header(default=None)):
    
    data = get_decoded_token_data(token)
    if not data["valid_token"] or data["role"] != "admin":
        return {
            "data":[],
            "error":"invalid token please try to login as admin",
            "message": "failed to create auction"
        }
    print("dfjkfdjk", product_info)
    product_info = dict(product_info)
    data = product_handler.create_new_product(product_info)
    
    return data

class OrderProduct(BaseModel):
    product_id: int
    purpose: str


@router.post('/order_product',
        tags=["User Routes"],
        description="**Route for creating product**")
def order_product(order_product_info: OrderProduct, 
    product_handler: object = Depends(product.ProductHandler),
    token: Union[str, None] = Header(default=None)):
    
    data = get_decoded_token_data(token)
    if not data["valid_token"]:
        return {
            "data":[],
            "error":"invalid token please try to login as admin",
            "message": "failed to create auction"
        }

    order_product_info = dict(order_product_info)
    data = product_handler.order_product(order_product_info["purpose"], order_product_info["product_id"], data)
    
    return data



@router.get('/all_user_ordered_product',
        tags=["User Routes"],
        description="**Route for ordered**")
def list_product_for_user( product_handler: object = Depends(product.ProductHandler),
        token: Union[str, None] = Header(default=None)):
    
    data = get_decoded_token_data(token)
    if not data["valid_token"] :
        return {
            "data":[],
            "error":"invalid token please try to login as admin",
            "message": "failed to create auction"
        }

    
    res = product_handler.user_order(data)
    
    return res




@router.get('/list_all_product',
        tags=["Common Routes"],
        description="**Route for ordered**")
def all_product( product_handler: object = Depends(product.ProductHandler),):
    
    

    
    res = product_handler.list_all_product()
    
    return res