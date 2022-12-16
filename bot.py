from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="5754170947:AAH9mfGndaWsm1iMGrytb2uBboYkPb2ce6s")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
	await update.approve()
	await bot.send_message(
		chat_id=update.from_user.id, 
		text=(
			"<b>🥳 Ваша заявка на вступление в чат AstroModules Offtop успешно принята"
			+ '\n\n☘️ Другие чаты и каналы создателей:'
			+ '\nAstroModules: @AstroModules'
			+ '\nAstroModulesChat: @AstroModulesChat'
			+ '\nHPV modules: @HPV_MODULES_VIP'
			+ '\nHackerPhone: @HACKER_PHONE_VIP</b>'
			+ '\nHackerPhoneChat: @HACKER_PHONE_VIP_CHAT'
			),
		parse_mode="HTML"
		)
	await bot.send_message(
		chat_id=-1001579966828,
		text=f"<b>Добро пожаловать в чат, <a href='tg://user?id={update.from_user.id}'>{update.from_user.first_name}</a>!</b>",
		parse_mode="HTML"
		)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
