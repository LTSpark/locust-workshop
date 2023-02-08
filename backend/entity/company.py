from datetime import datetime

from pydantic import BaseModel


class Company(BaseModel):
    id: int
    name: str
    slogan: str
    suffix: str
    phone_number: str
    created_at: datetime


class CreateCompany(BaseModel):
    name: str
    slogan: str
    suffix: str
    phone_number: str
