from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import requests
from pathlib import Path
from pydantic import BaseModel



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





@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/upload-excel")
async def upload_excel(file: UploadFile ):



    return {"file_name": file.filename}



