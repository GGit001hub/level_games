from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

nechatlig = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("3 talik savol",callback_data='uchtalik'),
            InlineKeyboardButton("5 talik savol",callback_data='beshtalik'),
        ],
        [
            InlineKeyboardButton("8 talik savol",callback_data='sakista'),
            InlineKeyboardButton("10 talik savol",callback_data='onta'),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish 🔙",callback_data='black')
        ]
    ]
)
