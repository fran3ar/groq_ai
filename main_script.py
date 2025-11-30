from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.choices[0].message["content"])
