import os
import requests
from dotenv import load_dotenv
from utils import load_faqs, match_faq
from openai_fallback import get_openai_response

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def handle_telegram_update(update):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    user_msg = message.get("text", "")

    faqs = load_faqs()
    reply = match_faq(user_msg, faqs)
    if not reply:
        reply = get_openai_response(user_msg)

    send_telegram_message(chat_id, reply)

def send_telegram_message(chat_id, text):
    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })
