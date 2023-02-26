#!/usr/bin/env python3

import logging
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatType
from answer import Message


class Config:
    message = Message

    # LoggerAppender
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

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
    async def startCommand(message: types.Message):
        await message.answer(Config.message.GREETINGS)
        logging.debug(message.text)

    @dp.message_handler(commands=['help'])
    async def helpCommand(message: types.Message):
        for command, descript in Config.message.COMMANDS.items():
            await message.answer("{0} - {1}".format(command, descript))
            logging.debug(message.text)

    @dp.message_handler(commands=['java'])
    async def javaLinkCommand(message: types.Message):
        await message.answer(Config.message.JAVA_LINK)
        logging.debug(message.text)


if __name__ == '__main__':
    conf = Config
    asyncio.run(conf.dp.start_polling())
