from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="5957205153:AAH-KLQiLw1Ucy9p3SWOe0EgvEsvaL8nGBU")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    await update.approve()
    await bot.send_message(chat_id=update.from_user.id, text="Добро пожаловать в канал Kisave | Менеджеры")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
