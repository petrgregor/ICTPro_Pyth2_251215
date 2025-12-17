import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Base

db = sqlalchemy.create_engine("sqlite:///C:/Users/Student/PycharmProjects/ICTPro_Pyth2_251215/m06_serialization/school.db")

Session = sessionmaker(bind=db)
session = Session()

Base.metadata.create_all(db)  # Toto reálně vytvoří databázový soubor
