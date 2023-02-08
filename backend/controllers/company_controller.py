from typing import List, Optional
from datetime import datetime

from faker import Faker
from fastapi import APIRouter, Response, HTTPException, status

from entity import Company, CreateCompany

faker = Faker()
company_router = APIRouter()


@company_router.post("/api/v1/company", response_model=Company)
async def create_company(company: CreateCompany, response: Response, test_failure: Optional[bool] = None):
    company_id = faker.random_int()
    if company_id % 7 == 0 and test_failure is True:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail="Bad ID: we have found a Teapot!"
        )

    response.status_code = 201
    return Company(
        id=company_id,
        name=company.name,
        slogan=company.slogan,
        suffix=company.suffix,
        phone_number=company.phone_number,
        created_at=datetime.now()
    )


@company_router.get("/api/v1/company", response_model=Company)
async def get_company():
    return Company(
        id=faker.random_int(),
        name=faker.company(),
        slogan=faker.catch_phrase(),
        suffix=faker.company_suffix(),
        phone_number=faker.phone_number(),
        created_at=datetime.now()
    )


@company_router.get("/api/v1/company/{quantity}", response_model=List[Company])
async def get_companies(quantity: int):
    companies = []
    for _ in range(quantity):
        companies.append(Company(
            id=faker.random_int(),
            name=faker.company(),
            slogan=faker.catch_phrase(),
            suffix=faker.company_suffix(),
            phone_number=faker.phone_number(),
            created_at=datetime.now()
        ))
    return companies


@company_router.put("/api/v1/company/{company_id}")
async def put_company(company_id: str):
    return {"msg": f"Updated Company Id: {company_id}", "state": "Everything is OK!"}


@company_router.delete("/api/v1/company/{company_id}")
async def delete_company(company_id: str):
    return {"msg": f"Deleted Company Id: {company_id}", "state": "Everything is OK!"}
