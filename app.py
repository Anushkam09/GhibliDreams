import os
from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import uuid
from utils import generate_ghibli_image

app = Flask(__name__)

# Route to serve images from the images folder
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route("/", methods=["GET", "POST"])
def home():
    loading = False
    error = False
    generated_image = None

    if request.method == "POST":
        prompt = request.form["prompt"]
        loading = True  # Set loading to True before generating the image
        try:
            image = generate_ghibli_image(prompt)
            filename = f"{uuid.uuid4().hex}.png"
            os.makedirs("images", exist_ok=True)
            image_path = os.path.join("images", filename)
            image.save(image_path)
            generated_image = filename
        except Exception as e:
            print(f"Error generating image: {e}")
            error = True
        loading = False

    return render_template("index.html", loading=loading, error=error, generated_image=generated_image)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
