from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


pul_tanlash =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Omadli o'yinlar"),
            KeyboardButton("Savollarga javoblar"),
        ],
        [
            KeyboardButton("🔀 Chalkash harflar"),
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
            KeyboardButton("🎲 Tosh tashlash"),
        ],
        [
            KeyboardButton("🔎 Harf topish"),
            KeyboardButton("🪜 Zinapoya"),
        ],
        [
            KeyboardButton("🔙 Orqaga qaytish")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)