from aiogram import types, Router, F
from aiogram.types import FSInputFile


catalog_router=Router()



@catalog_router.message(F.text.lower()=="поиск")
async def search(message: types.Message):
    await message.answer("введите название товара")



@catalog_router.message(F.text.lower() == "лек. для суставов")
async def systavi(message: types.Message):
    photo=FSInputFile('img/catalog/Teraflex_ultra.jpg')
    await message.answer_photo(photo)
    await message.answer("Терафлекс ультра, отличный меедикамент для больных суставов, всего за 3990 рублей")



@catalog_router.message(F.text.lower() == "лек. для сердечно-сосудистых заболеваний")
async def serdechno_sosyd(message: types.Message):
    photo_1= FSInputFile('img/catalog/Dristan_cold.jpg')
    await message.answer_photo(photo_1)
    await message.answer("Дристан колд лучшее лекарство в нашем асортименте, помогает от любых проблем, даже не связаных с сердечно-сосудистыми заболеваниями")



@catalog_router.message(F.text.lower() == "лек. для мышц")
async def mischc(message: types.Message):
    photo_2=FSInputFile("img/catalog/Draje_loxein.jpg")
    await message.answer_photo(photo_2)
    await message.answer("Драже лохеин поможет в любой ситуации, иногда даже при проблемах с мышцами")



@catalog_router.message(F.text.lower() == "лек. для лёгких заболеваний")
async def mischc(message: types.Message):
    photo_3=FSInputFile("img/catalog/")
    await message.answer_photo(photo_3)
    await message.answer("")




@catalog_router.message(F.text.lower() == "лек. для тяжёлых простудных заболеваний")
async def mischc(message: types.Message):
    photo_4=FSInputFile("img/catalog/")
    await message.answer_photo(photo_4)
    await message.answer("")



@catalog_router.message(F.text.lower() == "лек. для желудочных/кишечных заболеваний")
async def mischc(message: types.Message):
    photo_5=FSInputFile("img/catalog/")
    await message.answer_photo(photo_5)
    await message.answer("")