from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tikish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("5 $",callback_data="besh"),
            InlineKeyboardButton("10 $",callback_data="ong"),
        ],
        [
            InlineKeyboardButton("15 $",callback_data='onbesh'),
            InlineKeyboardButton("20 $",callback_data='yigirma'),            
        ],
        [
            InlineKeyboardButton("50 $",callback_data="ellik")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish 🔙",callback_data='back'),
            InlineKeyboardButton("💰 Hisobni ko'rish",callback_data='hisobnoma'),
        ]
    ]
)


omadni_sinash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1",callback_data="birga"),
            InlineKeyboardButton("2",callback_data="birga"),
            InlineKeyboardButton("3",callback_data='birga'),
            InlineKeyboardButton("4",callback_data='birga'),            
        ],
        [
            InlineKeyboardButton("5",callback_data="birga"),
            InlineKeyboardButton("6",callback_data="birga"),
            InlineKeyboardButton("7",callback_data='birga'),
            InlineKeyboardButton("8",callback_data='birga'),            
        ],
        [
            InlineKeyboardButton("9",callback_data="birga"),
            InlineKeyboardButton("10",callback_data="birga"),
            InlineKeyboardButton("11",callback_data='birga'),
            InlineKeyboardButton("12",callback_data='birga'),            
        ],
        [
            # InlineKeyboardButton("💰 Hisobni ko'rish",callback_data="hisobnoma"),
            InlineKeyboardButton("🔙 Orqaga qaytish",callback_data="orqaga")
        ]
    ]
)


rek_lama = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Tarqatish",switch_inline_query="rek"),
            InlineKeyboardButton("Ulashish",switch_inline_query="reklama")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish",callback_data="orqaga")
        ]
    ]
)

boshla = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton("O'yinni boshlash",callback_data='boshlash')
    ]]
)
