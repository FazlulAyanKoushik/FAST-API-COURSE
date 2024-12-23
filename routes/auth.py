from fastapi import APIRouter

auth_router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@auth_router.get("/login")
async def login():
    return {"message": "Login"}
