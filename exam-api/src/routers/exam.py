from datetime import date
from typing import List
from fastapi import APIRouter, Query
from fastapi_versioning import version


router = APIRouter(
    prefix="/exam",
    tags=["exam"]
)


@router.get("/")
@version(1)
async def list_exam():
    return {"exam": "api"}
