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



@dp.callback_query_handler(text="sticker",state=Marketnig.others)
async def Sticxona(call:CallbackQuery):
    xabar = "Stickerlar quyidagilardan iborat 👇"
    await call.message.answer(xabar,reply_markup=sticker_button)
    await call.message.delete()
    await User2State.sticker.set()


@dp.callback_query_handler(text="orqaga",state=User2State.sticker)
async def Orqaona(call:CallbackQuery):
    await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
    await call.message.delete()
    await Marketnig.others.set()



# 🦁 uchun handler
@dp.callback_query_handler(text="lion",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    kumush = int(select_users(userid)['kumush'])

    if kumush >= 199:
        qoldi_kum = kumush - 199
        update_baza('kumush',qoldi_kum,userid)
        update_others('sticker','🦁',userid)
        xabar = "Lion (🦁) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Kumushingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()



# 🐕 uchun handler
@dp.callback_query_handler(text="dog",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    kumush = int(select_users(userid)['kumush'])

    if kumush >= 159:
        qoldi_kum = kumush - 159
        update_baza('kumush',qoldi_kum,userid)
        update_others('sticker','🐕',userid)
        xabar = "Dog (🐕) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Kumushingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()






# 🐔 uchun handler
@dp.callback_query_handler(text="rooster",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    pul = int(select_users(userid)['pul'])

    if pul >= 449:
        qoldi_kum = pul - 449
        update_baza('pul',qoldi_kum,userid)
        update_others('sticker','🐓',userid)
        xabar = "<b>Rooster</b> (🐔) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await Marketnig.others.set()
        await call.message.delete()
    else:
        balo = await call.message.answer("Pulingiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()



# 🐈 uchun handler
@dp.callback_query_handler(text="cat",state=User2State.sticker)
async def lionxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    pul = int(select_users(userid)['pul'])

    if pul >= 399:
        qoldi_kum = pul - 399
        update_baza('pul',qoldi_kum,userid)
        update_others('sticker','🐈',userid)
        xabar = "<b>Cat</b> (🐈) muvofaqiyatli sotib olindi ✅"
        await call.message.answer(xabar,reply_markup=others_button)
        await call.message.delete()
        await Marketnig.others.set()
    else:
        balo = await call.message.answer("Pulngiz yetarli emas ❌")
        await asyncio.sleep(4)
        await balo.delete()
    


