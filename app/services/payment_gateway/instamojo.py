import os
from instamojo_wrapper import Instamojo

env = os.environ
API_KEY = env.get("INSTA_MOJO_API_KEY")
AUTH_TOKEN = env.get("INSTA_MOJO_AUTH_KEY")

api  = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, 
                endpoint= 'https://test.instamojo.com/api/1.1/')

class Instamojo:

    def __init__(self):
        pass

    def create_order(self, payload):
        response = api.payment_request_create(
            **payload
        )
        print(response, "lllllllllllllllll")
        return response

    def webhook(self, payload):
        pass

    def get_payment_status(self, order_id):
        response = api.payment_request_status(order_id)
        if "payment_request" in response:
            response = response["payment_request"]
        
        else:
            return {
                "message": "wrong order_id"
            }

        return {
            "status": response["status"],
            "payment": response["payments"],
            "payment_url":  response["longurl"]
        }