from sqlmodel import Session, create_engine, SQLModel
# from sqlalchemy import create_engine
from app.models.database_models import *
import os



# print("yes")

env = os.environ
mysql_root_host = env.get('MYSQL_ROOT_HOST')
mysql_username = env.get("MYSQL_USER")
mysql_port = env.get('MYSQL_PORT', 3306)
mysql_database = env.get("MYSQL_DATABASE")
mysql_password = env.get("MYSQL_PASSWORD")

URL = f"mysql://{mysql_username}:{mysql_password}@{mysql_root_host}:{mysql_port}/{mysql_database}"



# URL = "mysql://fynd_acad:fynd123@mysql_db:3306/fynd_acad" 
# URL = env.get("DB_URL")
# URL = "postgresql://encwsezklfjgzf:af5a4ed0df503805cd1cd5aacae46ccd2881ced1d01588916205e71881287ff9@ec2-35-168-194-15.compute-1.amazonaws.com:5432/d9gmak7qi2ssqh"
# print(URL, "******************")


engine = create_engine(URL)

print(engine, "lfdskffffffffffff")

def init_db():
    SQLModel.metadata.create_all(engine)
