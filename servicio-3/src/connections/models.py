import enum
import os

from dotenv import dotenv_values
from sqlalchemy import Boolean, Column, Enum, Float, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.types import DateTime

config = dotenv_values(".env")

db_host = os.getenv("MYSQL_HOST")
db_port = os.getenv("MYSQL_PORT")
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DATABASE")

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class AlertType(str, enum.Enum):
    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"

class Alerts(Base):
    __tablename__ = "alerts"

    id_alerta = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    value = Column(Float)
    version = Column(Integer)
    type = Column(Enum(AlertType), nullable=True)
    sended = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)



