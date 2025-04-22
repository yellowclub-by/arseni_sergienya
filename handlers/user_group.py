from aiogram import Router, types, F



group_router=Router()



No_words=["черёмуха","запупорка","пэм","решётка","видеорегистратор"]




@group_router.message(F.text)
async def no_words(message: types.Message):
    user_message=message.text.split(" ")
    for word in user_message:
        if word.lower() in No_words:
            await message.answer(F"{message.from_user.first_name} соблюдай правила!")
            await message.delete()
            break




