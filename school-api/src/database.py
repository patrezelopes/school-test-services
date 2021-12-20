import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pycommon_school_test.core_db import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
