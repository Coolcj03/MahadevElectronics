from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:UmGrrBFgYWuuOybxciyqrvTCYjRHvSFN@yamanote.proxy.rlwy.net:31457/railway")

# Create SQLAlchemy engine with connection pooling and retry settings
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verify connection before use
    pool_recycle=300,    # Recycle connections every 5 minutes
    pool_timeout=20,     # Wait up to 20 seconds for a connection
    max_overflow=10      # Allow up to 10 connections beyond pool_size
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
