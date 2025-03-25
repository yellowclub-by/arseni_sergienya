import asyncio
from aiogram import Bot,Dispatcher,types



TOKEN="8036154514:AAEAtt4RN9N1MLjjY37FsKTOpzRzv-HuQ_M"
bot=Bot(token=TOKEN)
dp=Dispatcher()



@dp.message()
async def echo(message: types.Message):
    await message.answer('бот на отпуске')



async def main():
    print('Bot has started')
    await dp.start_polling(bot)



asyncio.run(main())
