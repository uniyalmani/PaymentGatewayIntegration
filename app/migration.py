import os
from fastapi import FastAPI, Response, status
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from sqlalchemy import UniqueConstraint, String
from sqlalchemy import Column
from app.utilities.helpers import hash_password, verify_password, create_jwt_token
from app.utilities.dependencies import get_session
from app.models.database_models import Role, User



class Migratetion:
    def __init__(self):
        self.session = next(get_session())

    def create_role(self, role_name):
        try:
            role = Role(name=role_name)
            self.session.add(role)
            self.session.flush()
            self.session.commit()
            print("sucessfully added")
        except Exception as e:
            print(e)

    def create_admin(self, admin_data):
        try:
            hashed_password = hash_password(admin_data["password"])
            
            print(admin_data)

            admin = User(name=admin_data["name"].lower().strip(),
                        email=admin_data["email"].lower().strip(),
                        hashed_password=hashed_password,
                        role_name="admin",)

            self.session.add(admin)
            self.session.flush()
            self.session.commit()
            print("sucessfully created", admin_data)
        except Exception as e:
            print(e)
