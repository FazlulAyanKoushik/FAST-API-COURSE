from fastapi import FastAPI
from routes.auth import auth_router
from routes.order import order_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(order_router, prefix="/order")


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
