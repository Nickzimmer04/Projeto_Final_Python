from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.models import Base
import os

load_dotenv()

# Verifica se a aplicação está executando os testes
if os.getenv("TESTING") == "1":
    SQLALCHEMY_DATABASE_URL = "sqlite://"
else:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Criação do engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite")
    else {}
)

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
