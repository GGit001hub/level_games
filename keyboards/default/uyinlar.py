from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


pul_tanlash =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Omadli o'yinlar"),
            KeyboardButton("Savollarga javoblar"),
        ],
        [
            KeyboardButton("🛍 Reklama")
        ],
        [
            KeyboardButton("🔙 Orqaga qaytish")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)

level_up_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⚔️ Battle"),
            KeyboardButton("🎲 Tosh tashlash")
        ],
        [
            KeyboardButton("🔙 Orqaga qaytish")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)