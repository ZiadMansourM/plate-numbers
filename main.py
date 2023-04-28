from fastapi import FastAPI, File, UploadFile
from typing import Dict

from plate_recognition import recognize_plates

app = FastAPI()

@app.post("/predict")
async def recognize_plate(file: UploadFile = File(...)) -> Dict[str, str]:
    content = await file.read()
    plate_number = recognize_plates(content)
    return {"plate_number": plate_number}

@app.get("/")
async def home():
    return {"message": "Root Page"}

@app.get("/about")
async def about():
    return {"message": "About page"}

if __name__ == "__main__":
    import uvicorn
    import cv2
    uvicorn.run(app, host="0.0.0.0", port=8000)