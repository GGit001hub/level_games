from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp

from handlers.users.functions import select_users,update_baza
from states.Levels_state import Marketnig
from states.user2 import *
from keyboards.inline.savdo_button import (others_button,set_market,
                                            sticker_button,)
from keyboards.inline.savollar_buton import ha_yuq
from .funktions import select_others,update_others

import asyncio


# 🌟 uchun handler
@dp.callback_query_handler(text="star",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    kumush = int(select_users(userid)['kumush'])

    if kumush >= 99:
        qoldi_kum = kumush - 99
        update_baza('kumush',qoldi_kum,userid)
        update_others('sticker','🌟',userid)
        xabar = "Star (🌟) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Kumushingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()





# ⚡️ uchun handler
@dp.callback_query_handler(text="zap",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    pul = int(select_users(userid)['pul'])

    if pul >= 299:
        qoldi_kum = pul - 299
        update_baza('pul',qoldi_kum,userid)
        update_others('sticker','⚡️',userid)
        xabar = "Zap (⚡️) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("💵 Pulingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()


# ⚔️ uchun handler
@dp.callback_query_handler(text="swords",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    pul = int(select_users(userid)['pul'])

    if pul >= 250:
        qoldi_kum = pul - 250
        update_baza('pul',qoldi_kum,userid)
        update_others('sticker','⚔️',userid)
        xabar = "Swords (⚔️) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Pulingiz $ yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()



# ❤️ uchun handler
@dp.callback_query_handler(text="heart",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    kumush = int(select_users(userid)['kumush'])

    if kumush >= 109:
        qoldi_kum = kumush - 109
        update_baza('kumush',qoldi_kum,userid)
        update_others('sticker','❤️',userid)
        xabar = "Heart (❤️) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Kumushingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()



