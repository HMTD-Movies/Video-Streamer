from pyrogram import Client, idle
import os
from Bot.video_stream import app
API_ID = os.environ.get("API_ID",11973721)
API_HASH = os.environ.get("API_HASH","5264bf4663e9159565603522f58d3c18")
TOKEN = os.environ.get("TOKEN","5933906749:AAFgwZRU4tWlnaxRoJm9VW1n451RB7PoBQs")

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="Bot"),
)
bot.start()
app.start()
idle()
