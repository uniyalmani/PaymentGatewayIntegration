from pydantic import BaseModel, validator, EmailStr
from fastapi import APIRouter, Depends

from app.services.payment_gateway import load_payment_gateway



router = APIRouter()

class Instamojo(BaseModel):
    amount: float
    purpose: str
    buyer_name: str
    send_email: bool
    email: str
    

@router.get('/success',
        tags=["Test Routes For PaymentGateWay"],
        description="**Route for c**")
def sucess(payment_id, payment_status, payment_request_id):
    return {"message": "sucessfull", "payment_id": payment_id,
            "payment_status": payment_status,
            "payment_request_id": payment_request_id
                }


@router.post('/test/payment_gateway',
        tags=["Test Routes For PaymentGateWay"],
        description="**Route for testing paymentgateway**")
def payment_handler(payload :Instamojo):
    payload = dict(payload)
    print(payload)
    payload["redirect_url"] = 'http://localhost:8000/success'
    insta_mojo = load_payment_gateway("instamojo")
    res = insta_mojo.create_order(payload)
    res["order_id"] = res["payment_request"]["id"]
    res["payment_url"] = res["payment_request"]["longurl"]
    return res




@router.post('/orderstatus',
        tags=["Test Routes For PaymentGateWay"],
        description="**Route for geting payment status by id **")
def payment_handler(order_id: str):
    insta_mojo = load_payment_gateway("instamojo")
    response = insta_mojo.get_payment_status(order_id)
    return response

