from fastapi import Request
from sqlmodel import Session
from app.utilities.helpers import is_valid_token
from app.controllers.database_initializer import engine
from fastapi import APIRouter, Depends, Request, Response, HTTPException, Security


def get_decoded_token_data(auth_token):
    """return token data with key valid_token for validation"""

    print("***************")
    print(auth_token, "********************")
    decoded_data = is_valid_token(auth_token)
    return decoded_data


def get_session():
    """creating session for each request"""
    with Session(engine) as session:
        yield session



