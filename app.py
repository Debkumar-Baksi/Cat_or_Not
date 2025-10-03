from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("cat_model.h5")

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None
    if request.method == "POST":
        # Save uploaded image
        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Preprocess image
        img = image.load_img(filepath, target_size=(64,64))  # same size as training
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        result = model.predict(img_array)[0][0]
        prediction = "Cat 🐱" if result < 0.5 else "Not Cat ❌"
        prob = model.predict(img_array)[0][0]
        probability = f"{prob:.2f}"
        print(result)


        filename = file.filename

    return render_template("index.html", 
                        prediction=prediction,
                        filename=filename
                        )

if __name__ == "__main__":
    app.run(debug=True)
