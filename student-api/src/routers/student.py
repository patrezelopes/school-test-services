from datetime import date
from typing import List
from fastapi import APIRouter, Query, Depends
from fastapi_versioning import version
from src.database import SessionLocal
from sqlalchemy.orm import Session
from src.models import Student

router = APIRouter(
    prefix="/student",
    tags=["student"]
)


def get_db():
    db = SessionLocal()
    with db:
        yield db


@router.get("/")
@version(1)
async def list_student(db: Session = Depends(get_db)):
    return db.query(Student).all()
