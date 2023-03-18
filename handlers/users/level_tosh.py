from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from .functions import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.level_inline import *

import random as r
import asyncio

kutish = ["👀","🤑","👁","🙁","🙁"]
sovgalar = ["💎",3,5,5,5,5,5,5,5,7,10,10]

@dp.callback_query_handler(text="reply",state=LevelUp.tosh)
async def ToshSjak(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    date = await state.get_data()
    idn = date.get("user_id")
    user = select_users(idn)
    
    stic = r.choice(kutish)
    haz = await call.message.answer(f"{stic}")
    await asyncio.sleep(3)
    await haz.delete()

    puli = user[5]
    if puli >= 3:
        ayrish = puli - 3
        update_baza('pul',ayrish,idn)
        one_inline = r.choice(sovgalar)
        two_inline = r.choice(sovgalar)
        tri_inline = r.choice(sovgalar)

        # inline uchun cod 👇
        yutuqlar = InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton(f"{one_inline}",callback_data="none"),
                InlineKeyboardButton(f"{two_inline}",callback_data="none"),
                InlineKeyboardButton(f"{tri_inline}",callback_data="none"),
            ],[
                InlineKeyboardButton("🔄 Aylantirish",callback_data="reply"),
                InlineKeyboardButton("🔙 Orqaga 🔙",callback_data="orqaga"),
            ]])

        if one_inline == two_inline and one_inline == tri_inline:
            level_up(idn,one_inline)
            daraja = user[4].split(",")
            lvl = daraja[0]
            qoldiq = daraja[-1]
            await call.message.answer(f"✅ <b>Sizga 3 ta {one_inline} raqami tushdi</b>\
                \n🏆 Darajangiz ko'tarildi: {lvl} lvl {qoldiq}",reply_markup=yutuqlar)
            # await call.message.delete()
        else:
            await call.message.answer("🎲 Omadingiz kelmadi",reply_markup=yutuqlar)
            # await call.message.delete()
    else:
        await call.message.answer("Kechirasiz pulingiz yetarli emas\
            \n<b>1 marta tashlash: 3 $</b>",reply_markup=tosh_inline)
        # await call.message.delete()
        # await LevelUp.
