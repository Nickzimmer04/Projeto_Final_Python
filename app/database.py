from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.models import Base
import os

load_dotenv()

# URL de conexão com PostgreSQL, carregada das variáveis de ambiente
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Criação do engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criação da SessionLocal
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()