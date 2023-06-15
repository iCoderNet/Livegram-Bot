from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = "5291799706:AAHbLes_oZVGyeD9_hLgl6Uynzrjk2CUx6s")
dp = Dispatcher(bot)
adminid = 123135

@dp.register_message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hush kelibsiz")


@dp.register_message_handler()
async def start(message: types.Message):
    print(message)
    if message.forward:
        try:
            await bot.send_message(message.forward_from_chat, message.text)
            await message.reply("Yuborildi")
        except:
            await message.reply(f"Yuborilmadi\n\n{message}")
    else:
        await bot.forward_message(adminid, message.from_user.id, message.message_id)

executor.start_polling(dp, skip_updates=True)