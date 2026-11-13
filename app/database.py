from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

# URL de conexão com SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./pokedex.db"

# Criação do engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
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