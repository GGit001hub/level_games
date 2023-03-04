from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


tosh_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("❓",callback_data="none"),
            InlineKeyboardButton("❓",callback_data="none"),
            InlineKeyboardButton("❓",callback_data="none"),
        ],
        [
            InlineKeyboardButton("🔄 Aylantirish",callback_data="reply"),
            InlineKeyboardButton("🔙 Orqaga 🔙",callback_data="orqaga"),
        ]
    ]
)


inline_battle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔎 Zakovat",callback_data="zakovat"),
            InlineKeyboardButton("⚔️ 1 vs 1 battle ⚔️",callback_data="batl1vs1"),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish",callback_data="orqaga")
        ]
    ]
)



sorovnoma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha",callback_data="albatta"),
            InlineKeyboardButton("❌ Yo'q",callback_data="kechirasiz")
        ]
    ]
)



bekor_qilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("❌ Bekor qilish",callback_data="bekor")
        ]
    ]
)



boshlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🏁 Boshlash",callback_data="boshlash")
        ]
    ]
)




batl1vs1_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha",callback_data="uyniyman"),
            InlineKeyboardButton("❌ Yo'q",callback_data="yuq")
        ]
    ]
)