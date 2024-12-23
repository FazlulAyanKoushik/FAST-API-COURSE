from fastapi import APIRouter

order_router = APIRouter(
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@order_router.get("/")
async def read_order():
    return {"message": "Hello World, This is the order route"}
