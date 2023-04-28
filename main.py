from fastapi import FastAPI, File, UploadFile
from typing import Dict

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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

def recognize_plates(content):
    import cv2
    import numpy as np
    import imutils
    import easyocr
    
    nparr = np.frombuffer(content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    mask = np.zeros(gray.shape, np.uint8)

    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]

    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)

    return result[0][-2]

if __name__ == "__main__":
    import uvicorn
    import cv2
    uvicorn.run(app, host="0.0.0.0", port=8000)