from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


set_market = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💎 Kumushlar",callback_data="kumush"),
            InlineKeyboardButton("$ Pullar",callback_data="pul"),
        ],
        [
            InlineKeyboardButton("👩‍🌾 Fermachilik",callback_data="ferma"),
            InlineKeyboardButton("💰 Hisobni tekshirish",callback_data="hisob")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga 🔙",callback_data="nazat")
        ]
    ]
)


kumush_set = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1 ta 💎 = 59 $",callback_data="gems1"),
            InlineKeyboardButton("10 💎 = 549 $",callback_data="gems10"),
        ],
        [
            InlineKeyboardButton("1 ta 💎 = 0.59 US$",callback_data="uzs1"),
            InlineKeyboardButton("10 💎 = 1.99 US$",callback_data="uzs10"),
        ],
        [
            InlineKeyboardButton("🛍 Xaridlar bo'limiga qaytish 🔙",callback_data="magazin")
        ]
    ]
)




pull_set = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("10 $ = 0.3 US$",callback_data="shop1"),
            InlineKeyboardButton("50 $ = 0.49 US$",callback_data="shop5"),
        ],
        [
            InlineKeyboardButton("100 $ = 0.99 US$",callback_data="shop10"),
            InlineKeyboardButton("1000 $ = 9.99 US$",callback_data="shop15"),
        ],
        [
            InlineKeyboardButton("🛍 Xaridlar bo'limiga qaytish 🔙",callback_data="magazin")
        ]
    ]
)



set_ferma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🐰 1x quyon = 15 💎",callback_data="quyon1x"),
            InlineKeyboardButton("🐓 1x tovuq = 12 💎",callback_data="tovuq1x"),
        ],
        [
            InlineKeyboardButton("🐰 5x quyon = 69 💎",callback_data="quyon5x"),
            InlineKeyboardButton("🐓 5x tovuq = 55 💎",callback_data="tovuq5x"),
        ],
        [
            InlineKeyboardButton("🥕 1x sabzi = 12 $",callback_data="sabzi1"),
            InlineKeyboardButton("🌽 1x don = 9 $",callback_data="don1"),
        ],
        [
            InlineKeyboardButton("🥕 10x sabzi = 109 $ ",callback_data="sabzi10"),
            InlineKeyboardButton("🌽 10x don = 79 $",callback_data="don10"),
        ],
        [
            InlineKeyboardButton("🛍 Xaridlar bo'limiga qaytish 🔙",callback_data="magazin")
        ]
    ]
)




ichiga_kir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👈 Orqaga qaytish 👈",callback_data="orqa")
        ]
    ]
)