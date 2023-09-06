from fastapi import FastAPI, status, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.models.traveler import Traveler
from app.database.db import SessionLocal
from app.schemas.traveler import TravelerInfo
from typing import List
from datetime import date

app = FastAPI()
db = SessionLocal()
app.mount("/statis", StaticFiles(directory="./app/views/assets"), name="assets")
templates = Jinja2Templates(directory="./app/views")


@app.get("/", response_class=HTMLResponse)
async def home(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})


@app.get("/travelerform", response_class=HTMLResponse)
async def traveler(req: Request):
    return templates.TemplateResponse("travelerform.html", {"request": req})


@app.get("/travelers", response_model=List[TravelerInfo],
         status_code=status.HTTP_200_OK)
async def get_all_travelers():
    all_travelers = db.query(Traveler).all()
    return all_travelers


@app.get("/traveler/{traveler_id}", response_model=List[TravelerInfo], status_code=status.HTTP_200_OK)
async def get_traveler(traveler_id):
    one_traveler = db.query(Traveler).filter(Traveler.id == traveler_id)
    return one_traveler


'''@app.post("/traveler")
async def create_traveler(info: TravelerInfo):
    new_traveler = Traveler(
        date_in=info.date_in,
        country=info.country,
        doc_type=info.doc_type,
        doc_number=info.doc_number,
        date_expedition=info.date_expedition,
        traveler_name=info.traveler_name,
        traveler_surname=info.traveler_surname,
        traveler_second_surname=info.traveler_second_surname,
        gender=info.gender,
        born_date=info.born_date
    )
    db.add(new_traveler)
    db.commit()
    db.refresh(new_traveler)
    return RedirectResponse("/", status_code=status.HTTP_200_OK)'''


@app.post("/traveler")
async def create_traveler(
        date_in: date = Form(),
        country: str = Form(),
        doc_type: str = Form(),
        doc_number: str = Form(),
        date_expedition: date = Form(),
        traveler_name: str = Form(),
        traveler_surname: str = Form(),
        traveler_second_surname: str = Form(),
        gender: str = Form(),
        born_date: date = Form(),
):
    new_traveler = Traveler(
        date_in=date_in,
        country=country,
        doc_type=doc_type,
        doc_number=doc_number,
        date_expedition=date_expedition,
        traveler_name=traveler_name,
        traveler_surname=traveler_surname,
        traveler_second_surname=traveler_second_surname,
        gender=gender,
        born_date=born_date
    )
    db.add(new_traveler)
    db.commit()
    db.refresh(new_traveler)
    return new_traveler
