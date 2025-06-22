from fastapi import FastAPI, Request
from telegram_bot import handle_telegram_update

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    handle_telegram_update(data)
    return {"ok": True}
