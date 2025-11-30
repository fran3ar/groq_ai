from groq import Groq
import os

# API key
GROQ_API_KEY_value = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY_value:
    raise ValueError("La variable de entorno GROQ_API_KEY no está definida.")

client = Groq(api_key=GROQ_API_KEY_value)

completion = client.chat.completions.create(
    model="compound-mini",  # nombre correcto
    messages=[
        {
            "role": "user",
            "content": "Hola, probando la API de Groq."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="")
