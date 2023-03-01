from aiogram import Bot,Dispatcher,types,executor
import ls1.config as config
import random
bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(text=[1,2,3])
async def rando(message: types.Message):
    user = int(message.text)
    randomi = random.randint(1,3)
    if randomi == user:
        await message.reply(f"вы угодали правельный ответ: {randomi}")
    else:
        await message.reply(f"Ты лох: Число бота: {randomi}")

executor.start_polling(dp)
