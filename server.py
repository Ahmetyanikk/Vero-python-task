from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import requests

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
async def upload_excel(file: UploadFile):
    if not file.filename.endswith(".csv"):
        return JSONResponse(content={"error": "File must be in Excel (.csv) format"}, status_code=400)


    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    return {"message": "File successfully uploaded and processed."}
