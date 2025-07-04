#first test with openai
import base64
import openai
import os
from dotenv import load_dotenv

# Bild codieren in base64
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Statusausgabe
print("Demo-Foto-Analyse für:\n Client 1 = Masterschool \n Client 2 = Tim")

# API-Schlüssel laden
load_dotenv()
client1 = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client2 = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY2"))

# Bildpfad und base64-Kodierung
image_path = "Kassenbon3.jpg"
base64_image = encode_image(image_path)

# Anfrage an OpenAI senden (nutze GPT-4o oder GPT-4-turbo oder GPT-40-mini)
response = client1.chat.completions.create(
    model="gpt-4o-mini",  # oder gpt-4-turbo oder gpt-4o-mini
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text":
"Welche Produkte und Preise sind auf diesem Kassenbon zu sehen?"
        "Gib eine CSV Liste getrennt nach Food und Non-Food aus"
        "Die Preise haben eine Kennung A oder B, je nach Food oder Non-Food"
        "Gib die Summe der Food und die Summe der Non-Food Produkte an"
        "Pfand ist ein negativer Preis, egal ob er positiv angegeben ist"
                 },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=1000,
)

# Ausgabe
print(response.choices[0].message.content)
