from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F



user_router=Router()



@user_router.message(CommandStart())
async def start_bot(message: types.Message):
    await message.answer('bro, this bot sell medikamentiki')



@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Добро пожаловать, выберите раздел:")



@user_router.message(Command("search"))
async def search(message: types.Message):
    await message.answer("Введите название медикамента:")



@user_router.message(Command("card"))
async def card(message: types.Message):
    await message.answer("Ваша корзина:")



@user_router.message(Command("favourite"))
async def favourite(message: types.Message):
    await message.answer("Ваши любимые медикаменты:")



@user_router.message(Command("support"))
async def support(message: types.Message):
    await message.answer("Киньте на донат разрабу пжлстыы")



# @user_router.message(F.text.lower().contains("сто")|
#                      F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer('много')

