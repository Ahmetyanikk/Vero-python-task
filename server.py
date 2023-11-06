from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse


app = FastAPI()

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
