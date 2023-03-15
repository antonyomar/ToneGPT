# import asyncio
# import telegram
#
#
# async def main():
#     bot = telegram.Bot(token="5895616761:AAGCXvD-yY9jb0MsH-GLCgwumMj4c6nfFVk")
#     async with bot:
#         print(await bot.getMe())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

from telegram.ext import Updater, CommandHandler
import telegram
from queue import Queue

# Check for new message --> polling
updater = Updater("5895616761:AAGCXvD-yY9jb0MsH-GLCgwumMj4c6nfFVk", use_context=True)

# Allow to register handler --> command, text, video, audio, etc
dispatcher = updater.dispatcher


# Define a  command callback function
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello")


# Create a command handler
start_handler = CommandHandler("start", start)

# Add command handler to dispatcher
dispatcher.add_handler(start_handler)

# Start polling
updater.start_polling()
