import os
from fastapi import FastAPI, Response, status
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from app.utilities.helpers import hash_password, verify_password, create_jwt_token
from app.utilities.dependencies import get_session
from app.models.database_models import Role, User


class Authentication:
    def __init__(self):
        self.session = next(get_session())

    def create_user(self, user_data):
        try:
            print(user_data)
            hashed_password = hash_password(user_data["password"])
            role = user_data["role"].lower().strip()
            print(user_data)

            user = User(name=user_data["name"].lower().strip(),
                        email=user_data["email"].lower().strip(),
                        hashed_password=hashed_password,
                        role_name= role,)
            
            print(user, "lfkldkflkl")
            self.session.add(user)
            self.session.flush()
            self.session.commit()
            data = {"email": user_data["email"].lower().strip(), "role": role, "name": user["name"]}
            time = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
            token = create_jwt_token(data, time)
            print(token)
            return {
                "error": None,
                "data": [
                    {"token":
                    token}
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

            
    def authenticate_user(self, user_data):
        try:
            print("]]]]]]]]]]]")
            email, password, role = user_data["email"], user_data["password"], user_data["role"]
            email = email.lower().strip()
            print(email, password)
            query = select(User).where(User.email == email, User.role_name == role)
            user = self.session.exec(query).first()
            print(user, "llll")
            if verify_password(password, user.hashed_password):
                data = {"email": email, "role": role, "name": user.name}
                time = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
                token = create_jwt_token(data, time)
                return {
                "error": None,
                "data": [
                    {"token":
                    token}
                ],
                "message":"successfully login"
            }
            else:
                return {
                    "error": None,
                    "data": [
                        {"token":None
                           }
                    ],
                    "message":"failed to login"
                }
        except Exception as e:
            return  {
                    "error": None,
                    "data": [
                        {"token":None
                           }
                    ],
                    "message":"failed to login"
                }