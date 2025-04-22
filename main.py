import asyncio
from aiogram import Bot,Dispatcher




TOKEN="8036154514:AAEAtt4RN9N1MLjjY37FsKTOpzRzv-HuQ_M"
bot=Bot(token=TOKEN)
dp=Dispatcher()



from handlers.user_private import user_router
dp.include_router(user_router)



from handlers.user_group import group_router
dp.include_router(group_router)



async def main():
    print('Bot has started')
    await dp.start_polling(bot)             



asyncio.run(main())
