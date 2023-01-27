import os
from fastapi import FastAPI, Response, status
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from app.utilities.helpers import hash_password, verify_password, create_jwt_token
from app.utilities.dependencies import get_session
from app.models.database_models import Role, User, Product, OrderInfo
from app.services.payment_gateway import load_payment_gateway



class ProductHandler:
    def __init__(self):
        self.session = next(get_session())

    def create_new_product(self, product_info):
        try:

            product = Product(name=product_info["name"].lower().strip(),
                        amount=product_info["amount"],
                        discription=product_info["discription"],
                        )
            data = dict(product)
            self.session.add(product)
            
            self.session.commit()
            self.session.flush()

            return {
                "error": None,
                "data": [
                    {"product":
                    data}
                ],
                "message":"account created"
            }

        except Exception as e:
            return {
                "error": e,
                "data": [
                    {"token":
                    None}
                ],
                "message":"failed to create account"
            }

        


    def order_product(self, purpose, product_id, data):
        query = select(Product).where(Product.id == product_id)
        product_info = self.session.exec(query).first()
       
    
        if not product_info:
            return {
                "error" : "no auction exist",
                "data" : [],
                "message": "Auction is already soled"
            }

        product_info = dict(product_info)

        payload = {
        "amount": product_info["amount"],
        "purpose": purpose,
        "buyer_name": data["name"],
        "send_email": True,
        "email": data["email"]
        }

        payload["redirect_url"] = 'http://localhost:8000/success'

        insta_mojo = load_payment_gateway("instamojo")
        response = insta_mojo.create_order(payload)
        print(response)
        order_info = OrderInfo(order_id= response["payment_request"]["id"],
                    product_id=product_info["name"],
                    user_email=data["email"],
                     )

        order_info_dct = dict(order_info)
        self.session.add(order_info)
        self.session.flush()
        self.session.commit()
        return {
                "error" : None,
                "data" : [{ "payment_link": response["payment_request"]["longurl"],
                    "order_indfo":order_info_dct, 
                }],
                "message": "order succesfully placed"
            }
        
    def list_all_product(self):
        query = select(Product)
        result = self.session.exec(query).all()
        return {
                "error":None,
                "data": [
                    {
                        "all_product":result,
                    }
                ],
                "message": "sucessfull"
                            }

    def user_order(self, data):
        query = select(OrderInfo).where(OrderInfo.user_email == data["email"])
        order_info = self.session.exec(query).all()

        return {
                "error":None,
                "data": [
                    {
                        "order_info":order_info,
                    }
                ],
                "message": "sucessfull"
                            }

    def payment_info_by_order_id(self, order_id):
        insta_mojo = load_payment_gateway("instamojo")
        response = insta_mojo.get_payment_status(order_id)
        return response