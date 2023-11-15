from fastapi import FastAPI, File, UploadFile,Form,Body
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import requests
from pathlib import Path
from pydantic import BaseModel, conint, model_validator
from typing import Annotated
import json



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

class Item(BaseModel):
    keys: str
    colored: bool

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/upload-excel")
async def upload_excel(file: UploadFile = Form(...), json_data: str = Form(...)):
    contents = await file.read()

    return {"file_name": file.filename, "file_size": len(contents), "json_data": json_data}




