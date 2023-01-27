from typing import Any
import jwt

# for creating and veryfing jwt tocken
from passlib.context import CryptContext

# for hasing password
from datetime import datetime, timedelta

from fastapi import Request

# importing os
import os
import uuid
import json
from json import JSONEncoder



passlib_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




# make a UUID based on the host address and current time
def get_uuid():
    uuid_one = uuid.uuid1()
    return uuid_one



# subclass JSONEncoder for jsonifing
class DateTimeEncoder(JSONEncoder):
    # Override the default method
    """jasonify time"""
    def default(self, obj):
        return obj.isoformat()


# for verify password
def verify_password(plain_password, hashed_password):
    """verify password"""
    return passlib_context.verify(plain_password, hashed_password)


# for hashing password
def hash_password(password):
    """hashing passaword for storing in data base"""
    return passlib_context.hash(password)


# for creating jwt token
def create_jwt_token(data: dict, expire_time):
    """creating token for athurization"""
    to_encode = data.copy()
    expire_at = datetime.utcnow() + timedelta(minutes=expire_time)
    x = DateTimeEncoder().encode({"to_encode": expire_at})
    to_encode.update({"expire_at": x})
    env = os.environ
    token = jwt.encode(to_encode, env.get("SECRET_KEY"), algorithm="HS256")
    return token


# decoding token


def decode_token(token):
    """decoding token and return data"""
    try:
        env = os.environ
        data = jwt.decode(token, env.get("SECRET_KEY"), algorithms=["HS256"])
        print(data, "//////////////////")
        return data
    except Exception as e:
        print()
        return False


def validate_token_expiry(token_expiry_datetime):
    """return token is exppured or not """
    token_expiry_datetime = datetime.strptime(
        token_expiry_datetime, "%Y-%m-%dT%H:%M:%S.%f"
    )
    if token_expiry_datetime < datetime.now():
        return False
    return True


def is_valid_token(token):
    """validating token if exist """
    decoded_data = {}
    decoded_data["valid_token"] = False
    if token:
        decoded_data = decode_token(token) 
        if decoded_data:
            expire_at = json.loads(decoded_data["expire_at"])["to_encode"]
            valid_token = validate_token_expiry(expire_at)
            decoded_data["valid_token"] = valid_token
            return decoded_data
        
        decoded_data["valid_token"] = False

    return decoded_data

    