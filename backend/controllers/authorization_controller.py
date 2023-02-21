import hashlib

from fastapi import APIRouter

from entity import Auth

authorization_router = APIRouter()


@authorization_router.post("/api/v1/oauth")
async def auth(auth_request: Auth):
    to_encode = f'{auth_request.email}-{auth_request.password}'
    return {'token': f"{hashlib.md5(to_encode.encode()).hexdigest()}"}
