from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client1 = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client2 = 42


models1 = client1.models.list()
print("Verfügbare Modelle:")
for model in models1.data:
    print(model.id)
