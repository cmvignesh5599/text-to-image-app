{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "19811ae0-f4a9-4051-b517-b532440cd8c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.12/site-packages (2.32.2)\n",
      "Requirement already satisfied: pillow in /opt/anaconda3/lib/python3.12/site-packages (10.3.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/anaconda3/lib/python3.12/site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.12/site-packages (from requests) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/anaconda3/lib/python3.12/site-packages (from requests) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.12/site-packages (from requests) (2025.1.31)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests pillow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "00399435-71f6-43fd-85a2-65a7e71a8e4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import os\n",
    "import gradio as gr\n",
    "import requests\n",
    "from PIL import Image\n",
    "from io import BytesIO\n",
    "from dotenv import load_dotenv\n",
    "\n",
    "# Load API key from .env file\n",
    "load_dotenv()\n",
    "API_TOKEN = os.getenv(\"HF_API_KEY\")\n",
    "\n",
    "if not API_TOKEN:\n",
    "    raise ValueError(\"❌ ERROR: Hugging Face API key is missing. Set it in a .env file or as an environment variable.\")\n",
    "\n",
    "# Hugging Face model details\n",
    "MODEL_NAME = \"stabilityai/stable-diffusion-2\"\n",
    "URL = f\"https://api-inference.huggingface.co/models/{MODEL_NAME}\"\n",
    "HEADERS = {\"Authorization\": f\"Bearer {API_TOKEN}\"}\n",
    "\n",
    "def generate_image(prompt):\n",
    "    \"\"\"Generates an image from text using Hugging Face API.\"\"\"\n",
    "    response = requests.post(URL, headers=HEADERS, json={\"inputs\": prompt})\n",
    "    \n",
    "    if response.status_code == 200:\n",
    "        image = Image.open(BytesIO(response.content))\n",
    "        return image\n",
    "    else:\n",
    "        return f\"❌ API Error: {response.status_code} - {response.text}\"\n",
    "\n",
    "# Create Gradio Interface\n",
    "iface = gr.Interface(\n",
    "    fn=generate_image,\n",
    "    inputs=gr.Textbox(label=\"Enter Prompt\"),\n",
    "    outputs=\"image\",\n",
    "    title=\"AI Text-to-Image Generator\",\n",
    "    description=\"Enter a prompt and get an AI-generated image using Stable Diffusion!\",\n",
    ")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    iface.launch()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2cc852e9-92cc-4c0e-9a62-5d062dd06b34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Image generated successfully!\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a416e6a-df23-4029-8ac4-c468187b3cf2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c4ee6c8-8edb-48b4-a0d8-7ce68dc90db4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8db9c60-1cd9-4778-9b7a-09262254f1d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca9d41e0-471c-43d0-89d2-38d859601379",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "744f42a7-1d41-4370-9e3a-7401fef40780",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88669a2a-97e6-4566-9fde-9e238c8448b1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b5944bf-a078-4dbc-9928-1d285c0c8352",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6efb5fac-8fa0-42a4-897c-6e7c1bea1b72",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbfa415d-6a86-4692-af48-38d83e45d898",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82f2a783-e2d3-4b63-b904-745333c602d0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffa74345-467d-4254-822b-b7c347a1eda1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98b06cb4-3c08-4fd7-87df-d8c7b64efa17",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5a8392b-17aa-4461-8cbd-a2a37a45fb21",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ae28768-47de-4f7b-bf40-f27e96d818d4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5f68d68-93af-4eb0-8b11-eeb68ceb28af",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9e432ad-8f60-4ee2-b9c3-41f95b382b77",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa676d57-d61d-48a1-a34d-bc7d36f1ef9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4214b40-49f9-4c8b-b4af-1e6ebdefa330",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "474957d6-5b96-41fd-9a67-b62f044e1454",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8319812e-8933-45e9-9fbb-ca60f8da9bd1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "384ae3cc-702a-4227-8874-91e364384742",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "614013c3-abe4-4d9f-84cb-c08994fa1616",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8be50c60-6229-4b56-92a2-57a6e2bce982",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80947048-f1aa-4c73-9bab-8b3538c70846",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
