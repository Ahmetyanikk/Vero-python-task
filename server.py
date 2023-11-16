from fastapi import FastAPI, File, UploadFile,Form,Body
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import requests
from pathlib import Path
from pydantic import BaseModel, conint, model_validator
from typing import Annotated
import json
import pandas as pd



app = FastAPI()
url = "https://api.baubuddy.de/index.php/login"
payload = {
    "username": "365",
    "password": "1"
}
headers = {
    "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
    "Content-Type": "application/json"
}
response = requests.request("POST", url, json=payload, headers=headers)
temp=response.text.split('"')
print(temp[5])

def save_csv(file_contents: bytes, destination: Path):
    with open(destination, "wb") as file_object:
        file_object.write(file_contents)





@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/upload-excel")
async def upload_excel(file: UploadFile):
    contents = await file.read()

    # Specify the destination path to save the CSV file
    destination_path = Path(r"C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles") / file.filename

    # Save the CSV file
    save_csv(contents, destination_path)


    return {"File sent"}

@app.post("/Format-excel")
async def upload_excel(item: dict):
    Dfcsv = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles\vehicles.csv')
    colored= True
    if colored == True:
        try:
            for i in range(0, len(Dfcsv['hu'])):
                print("asd")
        except:
            print("error")



    return {"File sent"}




