#!/usr/bin/env python3

import logging
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatType
from datetime import datetime, date, time
from text import Message


class Config:
    message = Message

    # Logging
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

    # LoggerAppender
    file_handler = logging.FileHandler('logfile.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logging.getLogger().addHandler(file_handler)

    # Token API
    file = open("/home/fruitella/PycharmProjects/pythonProject/tgBot/resources/configuration.txt", "r")
    tokenValue = file.readline()
    bot = Bot(token=tokenValue)

    # Dispatcher session
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def start_command_handler(message: types.Message):
        await message.answer(Config.message.GREETINGS)
        logging.debug(message.text)

    @dp.message_handler(commands=['help'])
    async def help_command(message: types.Message):
        await message.answer(Config.message.COMMANDS)
        logging.debug(message.text)

    @dp.message_handler(commands=['time'])
    async def send_time(message: types.Message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.answer(text=f"Текущее время: {current_time}")
        logging.debug(message.text)


if __name__ == '__main__':
    conf = Config
    asyncio.run(conf.dp.start_polling())
