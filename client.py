from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import requests
app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

@app.get("/download-excel")
async def download_excel():
    file_path = "vehicles.csv"  # Replace with the actual path to your Excel file
    return FileResponse(file_path, filename="vehicles.csv")



