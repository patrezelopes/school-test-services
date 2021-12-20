from datetime import date
from typing import List
from fastapi import APIRouter, Query
from fastapi_versioning import version


router = APIRouter(
    prefix="/school",
    tags=["school"]
)


@router.get("/")
@version(1)
async def list_school():
    return {"school": "api"}
