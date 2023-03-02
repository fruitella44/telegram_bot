#!/usr/bin/env python3

import logging
import openai
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatType
from answers import Message
from pathD import Path


class Chat:
    message = Message
    pathD = Path

    # LoggerAppender
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )

    file_handler = logging.FileHandler("logfile.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logging.getLogger().addHandler(file_handler)

    # OPEN_AI_API
    fileOpenAI = open(pathD.TOKEN_OPENAI_API_PATH, "r")
    tokenOpenAI = fileOpenAI.readline()
    openai.api_key = tokenOpenAI

    # TG_API
    fileTG = open(pathD.TOKEN_TG_API_PATH, "r")
    tokenTG = fileTG.readline()
    bot = aiogram.Bot(token=tokenTG)
    dp = aiogram.Dispatcher(bot)

    @dp.message_handler(commands=["start"])
    async def startCommand(message: types.Message):
        await message.answer(Chat.message.GREETINGS)
        logging.debug(message.text)

    @dp.message_handler(commands=["help"])
    async def helpCommand(message: types.Message):
        for command, descript in Chat.message.COMMANDS.items():
            await message.answer("{0} - {1}".format(command, descript))
            logging.debug(message.text)

    @dp.message_handler(commands=["java"])
    async def javaLinkCommand(message: types.Message):
        await message.answer(Chat.message.JAVA_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=['python'])
    async def pythonLinkCommand(message: types.Message):
        await message.answer(Chat.message.PYTHON_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["sharp"])
    async def sharpLinkCommand(message: types.Message):
        await message.answer(Chat.message.SHARP_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["linux"])
    async def linuxLinkCommand(message: types.Message):
        await message.answer(Chat.message.LINUX_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["docker"])
    async def dockerLinkCommand(message: types.Message):
        await message.answer(Chat.message.DOCKER_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["db"])
    async def dataBaseLinkCommand(message: types.Message):
        await message.answer(Chat.message.DATA_BASE_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["confluence"])
    async def confluenceLinkCommand(message: types.Message):
        await message.answer(Chat.message.CONFLUENCE_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["admin"])
    async def activeDirectoryLinkCommand(message: types.Message):
        await message.answer(Chat.message.AD_LINK)
        logging.debug(message.text)

    @dp.message_handler(commands=["cv"])
    async def cvLinkCommand(message: types.Message):
        await message.answer(Chat.message.CV_LINK)
        logging.debug(message.text)

    @dp.message_handler()
    async def chatWithOpenAI(message: types.Message):
        prompt = message.text
        model_engine = "text-davinci-003"
        temperature = 0.5
        max_tokens = 4000
        n = 1
        stop = None

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n=n,
            stop=stop
        )

        await message.reply(response.choices[0].text)

    #TODO сделать кнопки в чате


if __name__ == "__main__":
    chat = Chat
    asyncio.run(chat.dp.start_polling())
