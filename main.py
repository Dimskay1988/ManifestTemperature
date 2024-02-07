from fastapi import FastAPI

from service import get_temperature

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Your app is up"}


@app.get("/get_temperature")
async def temperature():
    temp = get_temperature()
    return {"temperature": temp}
