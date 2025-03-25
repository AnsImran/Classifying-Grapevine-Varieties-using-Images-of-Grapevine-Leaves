from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
from tensorflow.keras import models




# Load the model along with it's weights
model = models.load_model('./model/Fine_Tuned_NN.keras')



# Input image shape used during training
TARGET_SIZE = (250, 250)



app = FastAPI()

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()

    try:
        # Load and preprocess the image
        image       = Image.open(io.BytesIO(contents)).convert("RGB")
        image       = image.resize(TARGET_SIZE)
        image_array = np.array(image) / 255.0                # Normalize like ImageDataGenerator
        image_array = np.expand_dims(image_array, axis=0)    # (1, 250, 250, 3)

        # Predict using the loaded model
        predicted_probabilities =  model.predict(image_array)
        predicted_label         =  int(np.argmax(predicted_probabilities, axis=1)[0])

        return {
            "filename":         file.filename,
            "predicted_label":  predicted_label,
            "probabilities":    predicted_probabilities.tolist()
        }

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
