import os
import openai
from aiogram import Bot, Dispatcher, executor, types

# Get secret key: https://platform.openai.com/account/api-keys
openai.api_key = "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"
bot = Bot(token="5895616761:AAGCXvD-yY9jb0MsH-GLCgwumMj4c6nfFVk")
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Hello :)')


@dispatcher.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Ou se trouve le mur de babel?",
        temperature=0.5,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    await message.reply(response.choices[0].text)

if __name__ == "__main__":
    executor.start_polling(dispatcher)