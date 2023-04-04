from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp

from handlers.users.functions import select_users,update_baza
from states.Levels_state import Marketnig
from states.user2 import *
from keyboards.inline.savdo_button import others_button,set_market
from keyboards.inline.savollar_buton import ha_yuq
from .funktions import select_others,update_others

import asyncio


@dp.callback_query_handler(text='others',state=Marketnig.bosh_holat)
async def Otehrscona(call:CallbackQuery):
    await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
    await call.message.delete()
    await Marketnig.others.set()




@dp.callback_query_handler(text="magazin",state=Marketnig.others)
async def Obasfa(call:CallbackQuery):
    await call.message.answer("Nima xarid qilasiz ❓",reply_markup=set_market)
    await call.message.delete()
    await Marketnig.bosh_holat.set()



## Taxmin 1x uchun handler 👇
## Taxmin 1x uchun handler  👇
## Taxmin 1x uchun handler   👇

@dp.callback_query_handler(text="taxmin1x",state=Marketnig.others)
async def Taxmin1x(call:CallbackQuery):
    xabar = "<b>1 ta yaxminni sotib olasizmi ? narxi 18 💎</b>\
        \nSotib olsangiz o'ynayotganda taxminlaar soni 1 taga ko'payadi"
    await call.message.answer(xabar,reply_markup=ha_yuq)
    await call.message.delete()
    await User2State.taxmin1.set()


@dp.callback_query_handler(text='yes',state=User2State.taxmin1)
async def Olamanxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))

    kumush = int(select_users(userid)['kumush'])
    if kumush >= 18:
        bor_taxmin = int(select_others(userid)['taxmin'])
        uzgar = bor_taxmin + 1
        qolgan_kumush = kumush - 18
        update_others('taxmin',uzgar,userid)
        update_baza('kumush',qolgan_kumush,userid)

        xabar = f"Sotib olish muvofaqiyatli tugadi ✅\
            \nSizda {uzgar} ta taxmin bor"
        await call.message.answer(xabar,reply_markup=others_button)
    else:
        balo = await call.message.answer("Sizda kumush yetarli emas")
        await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
        await asyncio.sleep(5)
        await balo.delete()
    await call.message.delete()
    await Marketnig.others.set()


@dp.callback_query_handler(text="no",state=User2State.taxmin1)
async def YoqTaxmin(call:CallbackQuery):
    await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
    await call.message.delete()
    await Marketnig.others.set()



## taxmin 2x uchun handler 👇
## taxmin 2x uchun handler  👇
## taxmin 2x uchun handler   👇


@dp.callback_query_handler(text="taxmin2x",state=Marketnig.others)
async def Taxmin1x(call:CallbackQuery):
    xabar = "<b>2 ta yaxminni sotib olasizmi ? narxi 35 💎</b>\
        \nSotib olsangiz o'ynayotganda taxminlaar soni 2 taga ko'payadi"
    await call.message.answer(xabar,reply_markup=ha_yuq)
    await call.message.delete()
    await User2State.taxmin2.set()


@dp.callback_query_handler(text='yes',state=User2State.taxmin2)
async def Olamanxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))

    kumush = int(select_users(userid)['kumush'])
    if kumush >= 35:
        bor_taxmin = int(select_others(userid)['taxmin'])
        uzgar = bor_taxmin + 2
        qolgan_kumush = kumush - 35
        update_others('taxmin',uzgar,userid)
        update_baza('kumush',qolgan_kumush,userid)

        xabar = f"Sotib olish muvofaqiyatli tugadi ✅\
            \nSizda {uzgar} ta taxmin bor"
        await call.message.answer(xabar,reply_markup=others_button)
    else:
        balo = await call.message.answer("Sizda kumush yetarli emas")
        await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
        await asyncio.sleep(5)
        await balo.delete()
    await call.message.delete()
    await Marketnig.others.set()


@dp.callback_query_handler(text="no",state=User2State.taxmin2)
async def YoqTaxmin(call:CallbackQuery):
    await call.message.answer("Profil xaridlar bo'limi",reply_markup=others_button)
    await call.message.delete()
    await Marketnig.others.set()



