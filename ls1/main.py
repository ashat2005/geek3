from aiogram import Bot,Dispatcher,types,executor
import ls1.config as config

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start',"go"])
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}, {message.from_user.url}")

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.reply("Вот мои комманды:")

@dp.message_handler(text=["привет"])
async def hi(message:types.Message):
    await message.answer("привет")

@dp.message_handler(commands=["about"])
async def about(message:types.Message):
    await message.answer(f"{message.from_user.as_json()}")
    await message.answer(f"First-name: {message.from_user.first_name},\n Name: {message.from_user.last_name},\n User-name: {message.from_user.username}")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSQQxkD6fJrPWXeiVHheXndqwyz-QWbo5EenqdsnI&s")
    await message.answer_location(40.519266414853945, 72.8029469994469)
    with open("/home/askhat/Desktop/geek3/photo_2023-01-30_09-16-37.jpg", "rb")as g:
        await message.answer_photo(g.read())
@dp.message_handler()
async def not_found(message:types.Message):
    await message.answer("Ваша команда не распознана, введите /help")

executor.start_polling(dp)