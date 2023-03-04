from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ruyxat_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🐰 Quyonlar",callback_data="rabbit"),
            InlineKeyboardButton("🐔 Tovuqlar",callback_data="chicken")
        ],
        [
            InlineKeyboardButton("Orqaga qaytish",callback_data="orqaga")
        ]
    ]
)


hal_qilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🥦 Ovqat berish",callback_data="ovqat")
        ],
        [
            InlineKeyboardButton("💰 Sotish 1x tasi",callback_data="sotish1")
        ],
        [
            InlineKeyboardButton("💰 Sotish 5x tasi",callback_data="sotish5")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish",callback_data="orqaga")
        ]

    ]
)



sotaman = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Sotaman",callback_data="ha"),
            InlineKeyboardButton("❌ Yo'q",callback_data="yuq"),
        ]
    ]
)


qaytish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔙 Orqaga qaytish 🔙",callback_data="urqa")
        ]
    ]
)
