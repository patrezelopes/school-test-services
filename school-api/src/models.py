from sqlalchemy import Column, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = "core_school"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
