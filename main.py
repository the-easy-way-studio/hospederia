from fastapi import FastAPI, status
from app.models.traveler import Traveler
from app.database.db import SessionLocal
from app.schemas.traveler import TravelerInfo
from typing import List

app = FastAPI()
db = SessionLocal()


@app.get("/travelers", response_model=List[TravelerInfo],
         status_code=status.HTTP_200_OK)
async def get_all_travelers():
    all_travelers = db.query(Traveler).all()
    return all_travelers


@app.post("/traveler", response_model=TravelerInfo,
          status_code=status.HTTP_201_CREATED)
async def create_traveler(info: TravelerInfo):
    new_traveler = Traveler(
        id=None,
        date_in=Traveler.date_in,
        country=Traveler.country,
        doc_type=Traveler.doc_type,
        doc_number=Traveler.doc_number,
        date_expedition=Traveler.date_expedition,
        traveler_name=Traveler.traveler_name,
        traveler_surname=Traveler.traveler_surname,
        traveler_second_surname=Traveler.traveler_second_surname,
        gender=Traveler.gender,
        born_date=Traveler.born_date
    )
    db.add(new_traveler)
    db.commit()
    return new_traveler


@app.get("/traveler/{item}")
async def traveler(item):
    return item
