from sqlalchemy import String, Column, Integer, Date

from app.database.db import Base, engine
from datetime import date


def create_table():
    Base.metadata.create_all(engine)


class Traveler(Base):
    __tablename__ = 'travelers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_in = Column(Date, nullable=False)
    country = Column(String(80), nullable=False)
    doc_type = Column(String(1), nullable=False)
    doc_number = Column(String(25), nullable=False)
    date_expedition = Column(Date, nullable=False)
    traveler_name = Column(String(25), nullable=False)
    traveler_surname = Column(String(25), nullable=False)
    traveler_second_surname = Column(String(25), nullable=False)
    gender = Column(String(1), nullable=False)
    born_date = Column(Date, nullable=False)
