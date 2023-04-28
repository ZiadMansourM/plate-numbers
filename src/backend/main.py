from fastapi import FastAPI, File, UploadFile
from typing import Dict

import plate_recognition

app = FastAPI()

@app.post("/recognize_plate")
async def recognize_plate(file: UploadFile = File(...)) -> Dict[str, str]:
    content = await file.read()
    plate_number = plate_recognition.recognize_plates(content)
    return {"plate_number": plate_number}

@app.get("/")
async def home():
    return {"message": "Root Page"}

@app.get("/about")
async def about():
    return {"message": "About page"}