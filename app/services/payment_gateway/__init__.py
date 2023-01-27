from app.resources.exceptions import InvalidPaymentGatewayException
from app.resources.constants import PaymentGatewayEnum
from .cashfree import CashFree
from .instamojo import Instamojo

def load_payment_gateway(payment_gateway):
    print(payment_gateway, PaymentGatewayEnum.instamojo)
    if payment_gateway == PaymentGatewayEnum.cashfree.name:
        return CashFree()

    elif payment_gateway == PaymentGatewayEnum.instamojo.name:
        return Instamojo()
    else:
        raise InvalidPaymentGatewayException(f"Payment gatewa: {payment_gateway} doesn't exist.")