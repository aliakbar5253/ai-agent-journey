from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what an AI agent is in 3 sentences, for a BCA student.",
)

print(response.text)