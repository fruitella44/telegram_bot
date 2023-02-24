#!/usr/bin/env python3

import os
import logging
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatType
from  datetime import datetime, date, time

class Config:

    # Logging into console
    logging.basicConfig(level=logging.INFO)

    # Token API
    token = os.environ.get('TELEGRAM_BOT_TOKEN')

    # Dispatcher session
    dp = Dispatcher(token)

    @dp.message_handler(commands=['start'])
    async def start_command_handler(message: types.Message):
        await message.answer("Привет! Это fruitellaBot, чем могу помочь?")

    @dp.message_handler(commands=['help'])
    async def help_command(message: types.Message):
        await message.answer("Список доступных комманд:\n"
                             "/time - Показать текущее время")
        #TODO дописать команды

    @dp.message_handler(commands=['time'])
    async def send_time(message: types.Message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.answer(text=f"Текущее время: {current_time}")

if __name__ == '__main__':
    conf = Config
    asyncio.run(conf.dp.start_polling())