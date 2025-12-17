from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), nullable=False)
    surname = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name: str, surname: str, age: int, **kw: Any):
        super().__init__(**kw)
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return (f"Student(id={self.id}, name={self.name}, "
                f"surname={self.surname}, age={self.age})")