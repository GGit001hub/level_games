from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔒 Parolni almashtirish",callback_data="password")
        ],
        [
            InlineKeyboardButton("👤 Ismni almashtirish",callback_data="name_change")
        ],
        [
            InlineKeyboardButton("❌ Chiqib ketish",callback_data="loguot")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish",callback_data="orqaga")
        ]
    ]
)

chiqasizmi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha",callback_data="yes"),
            InlineKeyboardButton("❌ Yo'q",callback_data="net")
        ]
    ]
)


login = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📃 Ro'yxatdan o'tish",callback_data="register")
        ],
        [
            InlineKeyboardButton("🔑 Hisobga kirish",callback_data="login")
        ]
    ]
)
