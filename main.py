from fastapi import FastAPI, Request
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.webhook import get_new_configured_app
import sqlite3
import os

API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN_HERE")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
app = FastAPI()

@app.on_event("startup")
async def startup():
    print("Bot is starting...")

@app.post("/")
async def telegram_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.process_update(telegram_update)
    return {"ok": True}

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.reply("Привет! Я AdjUSD_bot. Готов к работе.")