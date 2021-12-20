from sqlalchemy import Column, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = "core_exam"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    discipline = Column(String)
