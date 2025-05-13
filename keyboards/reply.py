from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



back_btn=KeyboardButton(text='назад')



main_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"),
         KeyboardButton(text="избранное")],
        [KeyboardButton(text="частые вопросики"),
         KeyboardButton(text="корзина")]
    ],
    resize_keyboard=True,
    input_field_placeholder="дарова кент, что хочешь?"
)



catalog_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="поиск")],
        [KeyboardButton(text="лек. для суставов"),
        KeyboardButton(text="лек. для мышц")],
        [KeyboardButton(text="лек. для лёгких заболеваний"),
        KeyboardButton(text="лек. для тяжёлых простудных заболеваний")],
        [KeyboardButton(text="лек. для желудочных/кишечных заболеваний"),
         KeyboardButton(text="лек. для сердечно-сосудистых заболеваний")],
        [back_btn]
    ],
    resize_keyboard=True,
    input_field_placeholder="дарова кент, что хочешь?"
)

