from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Replace with your actual database URL
DATABASE_URL = "postgresql://postgres:Abhi54321@employeeapplication.cfmoymyy5ibk.us-east-2.rds.amazonaws.com:5432/employeeApplication"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
