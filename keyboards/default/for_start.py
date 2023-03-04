from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_uvhun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("☎ Nomer yuborish 📞",request_contact=True)
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)




level_games = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Darajani ko'tarish"),
            KeyboardButton("Pul topish"),
        ],
        [
            KeyboardButton("🛍 Xaridlar"),
            KeyboardButton("Boshqalar...")
        ],
        [
            KeyboardButton("⚙️ Sozlamalar")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)