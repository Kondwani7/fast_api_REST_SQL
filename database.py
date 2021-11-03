from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()
user = os.getenv("DB_USER")
db = os.getenv("DB")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

engine = create_engine(f"postgresql://{user}:{password}@localhost:3306/{db}",
 echo=True)
Base = declarative_base()

SessionalLocal = sessionmaker(bind=engine)