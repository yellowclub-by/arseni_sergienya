from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton



def question():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="1 question",callback_data="question_1"),
        InlineKeyboardButton(text="2 question", callback_data="question_2"),
        InlineKeyboardButton(text="3 question", callback_data="question_3"),
        width=1
    )
    return builder.as_markup()