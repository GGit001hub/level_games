from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


zinalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🎲 Tosh tashlash",callback_data="aylantir"),
            InlineKeyboardButton("🎁 Sov'ga ochish",callback_data="sovga")
        ],
        [
            InlineKeyboardButton("👈 Orqaga qaytish",callback_data='orqaga')
        ]
    ]
)
