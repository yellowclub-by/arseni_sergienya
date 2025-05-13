from aiogram import types, Router, F
from aiogram.types import FSInputFile


catalog_router=Router()



@catalog_router.message(F.text.lower()=="поиск")
async def search(message: types.Message):
    await message.answer("введите название товара")

@catalog_router.message(F.text.lower() == "лек. для суставов")
async def search(message: types.Message):
    photo=FSInputFile('img/catalog/Терафлекс ультра.jng')
    await message.answer_photo(photo)
    await message.answer("Терафлекс ультра, отличный меедикамент для больных суставов, всего за 3990 рублей")

@catalog_router.message(F.text.lower() == "лек. для сердечно-сосудистых заболеваний")
async def search(message: types.Message):
    photo_1= FSInputFile('img/catalog/Дристан колд.jng')
    await message.answer_photo(photo_1)
    await message.answer("Дристан колд лучшее лекарство в нашем асортименте, помогает от любых проблем, даже не связаных с сердечно-сосудистыми заболеваниями")