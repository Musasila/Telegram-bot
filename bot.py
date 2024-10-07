import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

API_TOKEN = '6731743916:AAEkVaf69ge1_VfK-rNm91sAX9-dyjTls7E'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher with MemoryStorage
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start command
    """
    await message.reply("Salom!\nMen EchoBotman!\naiogram orqali ishlayapman.")


@dp.message_handler(Command("help"))
async def send_help(message: types.Message):
    """
    This handler will be called when user sends /help command
    """
    await message.reply("Yordam kerakmi?\nMen EchoBotman!\nAiogram kuchli foydalanvomonam.")


@dp.message_handler()
async def echo(message: types.Message, state: FSMContext):
    """
    This handler will be called for any other message
    """
    await message.answer(message.text)


async def on_startup(dp):
    """
    This function will be called on bot startup
    """
    await bot.send_message(chat_id="YOUR CHAT ID", text="Bot is started")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(on_startup(dp))
    executor.start_polling(dp)

