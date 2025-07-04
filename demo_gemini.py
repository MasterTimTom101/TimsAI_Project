import google.generativeai as genai
import base64
import os
from PIL import Image
from dotenv import load_dotenv

# Set API Key
load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

# Bild vorbereiten
image_path = "Kassenbon3.jpg"
with open(image_path, "rb") as img_file:
    image_bytes = img_file.read()

# Modell laden
model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt + Bild senden
response = model.generate_content(
    [
        "Welche Produkte und Preise sind auf diesem Kassenbon zu sehen?"
        "Gib eine CSV Liste getrennt nach Food und Non-Food aus"
        "Die Preise haben eine Kennung A oder B, je nach Food oder Non-Food"
        "Gib die Summe der Food und die Summe der Non-Food Produkte an"
        "Pfand ist ein negativer Preis, egal ob er positiv angegeben ist",
        {"mime_type": "image/jpeg", "data": image_bytes}
    ]
)

# Ausgabe
print(response.text)
