from fastapi import FastAPI, File, UploadFile,Form,Body
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import requests
from pathlib import Path
from pydantic import BaseModel, conint, model_validator
from typing import Annotated
import json
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side
from datetime import datetime

def color_rows(row):
    today = datetime.today()
    if (today - row['hu']).days <= 90:
        return ['background-color: #007500'] * len(row)
    elif (today - row['hu']).days <= 365:
        return ['background-color: #FFA500'] * len(row)
    else:
        return ['background-color: #b30000'] * len(row)


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
headers = {
    'Authorization': f'Bearer {temp[5]}',
    'Content-Type': 'application/json',
}


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
async def upload_excel():
    response = requests.get("https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active", headers=headers)
    responseJson = response.json()
    responseCsv = pd.DataFrame(responseJson)
    Dfcsv = pd.read_csv(r'C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles\vehicles.csv',on_bad_lines='skip')
    Dfcsv.to_csv(r'C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles\\'+"filename"+".csv")
    merged_df = pd.concat([responseCsv, Dfcsv],axis=1)
    merged_df.sort_values(by='gruppe')
    colored= True
    if colored == True:
        try:
            styled_df = merged_df.style.apply(color_rows, axis=1)

        except:
            print("error")
    current_date_iso_formatted = datetime.now().date().isoformat()
    filename="vehicles_"+current_date_iso_formatted+".xlsx"
    merged_df.to_excel(r'C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles\\'+filename)

    return FileResponse(r'C:\Users\Ahmet\PycharmProjects\pythonProject1\Serverfiles\\', filename=filename)


