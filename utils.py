import os
import openai
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ghibli_image(prompt, size="1024x1024"):
    final_prompt = f"{prompt} in Ghibli studio themed style"
    print(f"🎨 Prompt sent: {final_prompt}")
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=final_prompt,
            n=1,
            size=size,
            response_format="url"
        )
        image_url = response.data[0].url
        print(f"🔗 Image URL: {image_url}")

        # Download the image and return the image object
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        image = Image.open(BytesIO(img_response.content)).convert("RGB")

        return image  # Return image to Flask
    except Exception as e:
        print("❌ Error occurred:", e)
        return None

def test():
    prompt = input("Enter prompt: ")
    image, url = generate_ghibli_image(prompt)
    if image:
        save_path = "./images/ghibli_output.png"
        image.save(save_path)
        print(f"✅ Image saved as {save_path}")
        print(f"🔗 Image URL: {url}")
    else:
        print("❌ Image could not be saved.")

if __name__ == "__main__":
    test()