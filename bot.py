import requests
from telegram import Bot
from datetime import datetime
import os
import asyncio

API_KEY_WEATHER = os.getenv("API_KEY_WEATHER")
API_TELEGRAM = os.getenv("API_TELEGRAM")
CHANNEL = os.getenv("CHANNEL")

LAT = -0.75
LON = -78.95

def obtener_clima():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY_WEATHER}&units=metric&lang=es"
    data = requests.get(url).json()

    temp = data["main"]["temp"]
    clima = data["weather"][0]["description"]

    return f"""
🌤 *Clima Aproximado Chugchilán (basado en Sigchos)*
🕒 {datetime.now().strftime('%d-%m-%Y %H:%M')}
🌡 Temperatura: {temp}°C
☁ Condición: {clima}
"""

async def enviar():
    bot = Bot(API_TELEGRAM)
    await bot.send_message(chat_id=CHANNEL, text=obtener_clima(), parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(enviar())
