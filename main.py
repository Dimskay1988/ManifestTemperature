from fastapi import FastAPI
from pydantic import BaseModel

from service import get_temperature

import json

app = FastAPI()


class UpdateDataDevice(BaseModel):
    sensor_address: str


@app.get("/")
async def read_root():
    return {"message": "Your app is up"}


@app.get("/get_temperature")
async def temperature():
    url = read_data().get("sensor_address")
    temp = get_temperature(url)
    return {"temperature": temp}


json_file_path = "data.json"


def read_data():
    with open(json_file_path, "r") as file:
        data = json.load(file)
    return data


def write_data(data):
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)


@app.get("/get_device", description="An example of what the device address should be http://192.168.1.151")
async def read_data_endpoint():
    return read_data()


@app.put("/update_device", description="An example of what the device address should be http://192.168.1.151")
async def update_data_endpoint(request_data: UpdateDataDevice):
    current_data = read_data()
    current_data.update(request_data)
    write_data(current_data)
    return {"message": "Data updated successfully"}
