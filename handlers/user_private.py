from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from keyboards import reply, inline



user_router=Router()



@user_router.message(CommandStart())
async def start_bot(message: types.Message):
    await message.answer('bro, this bot sell medikamentiki', reply_markup=reply.main_kb)



@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("""<b>Добро пожаловать</b>, выберите раздел:""", reply_markup=reply.catalog_kb)



# @user_router.message(Command("search"))
# async def search(message: types.Message):
#     await message.answer("Введите название медикамента:")



@user_router.message(Command("card"))
async def card(message: types.Message):
    await message.answer("Ваша корзина:",reply_markup=inline.links_kb)



@user_router.message(Command("favourite"))
async def favourite(message: types.Message):
    await message.answer("Ваши любимые медикаменты:")



@user_router.message(F.text.lower().contains("частые вопросики"))
@user_router.message(Command("question"))
async def question(message: types.Message):
    await message.answer("какой вопрос хотите задать???",reply_markup=inline.question())



@user_router.callback_query(F.data.lower().startswith('question'))
async def question_answer(callback:types.CallbackQuery):
    query=callback.data.split("_")[1]
    if query=='1':
        await callback.message.answer("first answer")
    elif query=='2':
        await callback.message.answer("second answer")
    elif query == '3':
        await callback.message.answer("third answer")
    await callback.answer('ответ отправлен')

@user_router.message(F.text.lower()=="назад")
async def back_menu(message: types.Message):
    await message.answer("главное меню",reply_markup=reply.main_kb)


# @user_router.message(F.text.lower().contains("сто")|
#                      F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer('много')

