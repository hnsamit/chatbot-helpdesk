import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=100,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I'm unable to process your request right now."
