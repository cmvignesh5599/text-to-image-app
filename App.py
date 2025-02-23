import os
import gradio as gr
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_TOKEN = os.getenv("HF_API_KEY")

if not API_TOKEN:
    raise ValueError("❌ ERROR: Hugging Face API key is missing. Set it in a .env file or as an environment variable.")

# Hugging Face model details
MODEL_NAME = "stabilityai/stable-diffusion-2"
URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt):
    """Generates an image from text using Hugging Face API."""
    response = requests.post(URL, headers=HEADERS, json={"inputs": prompt})
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"

# Create Gradio Interface
iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter Prompt"),
    outputs="image",
    title="AI Text-to-Image Generator",
    description="Enter a prompt and get an AI-generated image using Stable Diffusion!",
)

if __name__ == "__main__":
    iface.launch()
