from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



def question():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="1 question",callback_data="question_1"),
        InlineKeyboardButton(text="2 question", callback_data="question_2"),
        InlineKeyboardButton(text="3 question", callback_data="question_3"),
        width=1
    )
    return builder.as_markup()



links_kb=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='sait',url='https://yandex.ru/games/app/260283#app-id=260283&catalog-session-uid=catalog-26383e54-1157-578e-9b97-6d800820e8c5-1747758696844-b65a&rtx-reqid=4474020947418705482&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22search%22%7D&redir-data=%7B%22block%22%3A%22search%22%2C%22block_index%22%3A2%2C%22card%22%3A%22adaptive_recommended_new%22%2C%22col%22%3A0%2C%22first_screen%22%3A0%2C%22page%22%3A%22search%22%2C%22rn%22%3A358843406%2C%22row%22%3A0%2C%22rtx_reqid%22%3A%227839699906627523135%22%2C%22same_block_index%22%3A0%2C%22wrapper%22%3A%22grid-list%22%2C%22request_id%22%3A%221747758709574887-6867056464576652135-gq3pz34xiyls3ovx-BAL%22%2C%22games_request_id%22%3A%221747758709557173-16536238911418225879-balancer-l7leveler-kubr-yp-klg-169-BAL%22%2C%22http_ref%22%3A%22https%253A%252F%252Fyandex.ru%252Fgames%252Fsearch%253Fquery%253D%2525D1%252581%2525D1%252582%2525D0%2525B0%2525D0%2525BD%2525D0%2525B4%2525D0%2525BE%2525D1%252584%2525D1%252584%22%7D&search_query=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%BE%D1%84%D1%84'),
     InlineKeyboardButton(text='sait N2',url='https://yandex.ru/games/app/413380#app-id=413380&catalog-session-uid=catalog-26383e54-1157-578e-9b97-6d800820e8c5-1747759265081-0daf&rtx-reqid=7839699906627523135&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22for_girls%22%7D&redir-data=%7B%22block%22%3A%22cat_for_girls%22%2C%22block_index%22%3A1%2C%22card%22%3A%22adaptive_recommended_new%22%2C%22col%22%3A2%2C%22first_screen%22%3A1%2C%22page%22%3A%22cat_for_girls%22%2C%22rn%22%3A750056189%2C%22row%22%3A1%2C%22rtx_reqid%22%3A%227839699906627523135%22%2C%22same_block_index%22%3A0%2C%22wrapper%22%3A%22grid-list%22%2C%22request_id%22%3A%221747759263573224-13214649800070504522-dmhos7ujuvjnjbof-BAL%22%2C%22games_request_id%22%3A%221747759263554794-16899316828452515343-balancer-l7leveler-kubr-yp-klg-169-BAL%22%2C%22http_ref%22%3A%22https%253A%252F%252Fyandex.ru%252Fgames%252Fcategory%252Ffor_girls%22%7D'),
     InlineKeyboardButton(text='tg',url='https://myfin.by/wiki/term/cena-na-neft-na-segodnya-online')
    ]
]
)