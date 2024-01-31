# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Database details
# DB_HOST = '34.100.182.69'
# DB_PORT = '3306'
# DB_NAME = 'cloudnativedb'
# DB_USER = 'your_database_user'
# DB_PASSWORD = 'your_database_password'
# CLOUD_SQL_CONNECTION_NAME = 'gcp-data-project-410116:asia-south1:cloudnativedb-instance1'

# connection_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Database configuration settings
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/medical"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
