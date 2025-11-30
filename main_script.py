from groq import Groq
import os

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.choices[0].message["content"])
