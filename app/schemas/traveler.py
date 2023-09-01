from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class TravelerInfo(BaseModel):
    id: Optional[int] = None
    date_in: date
    country: str
    doc_type: str
    doc_number: str
    date_expedition: date
    traveler_name: str
    traveler_surname: str
    traveler_second_surname: str
    gender: str
    born_date: date
