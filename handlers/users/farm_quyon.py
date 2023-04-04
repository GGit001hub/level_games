from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from .functions import *
from .function_farm import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.farm_inline import *

import random as r
import asyncio,aiogram


@dp.callback_query_handler(text="rabbit",state=Farms.bosh_holat)
async def Quyon_xona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    bor = int(about['quyon']) ## 2 - element bu quyon
    sabzi = int(about['sabzi']) ## 4 - element bu sabzilar
    levl = about['lvlquyon'].split(",")[0]
    if bor >=1:
        await call.message.answer(f"🐰 <b>Sizni quyonlaringiz</b>\n✅ <b>Jami: {bor} ta</b> \
            \n🥕 Sabzilar: {sabzi} ta \n🏆 Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.quyon.set()
    else:
        baol = await call.message.answer("Sizda quyon yo'q")
        await asyncio.sleep(3)
        await baol.delete()



@dp.callback_query_handler(text="orqaga",state=Farms.quyon)
async def Sidawn(call:CallbackQuery):
    await call.message.answer("👉 Ferma bo'limi 👩‍🌾",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()



## Quyonga ovqat berish uchun code 👇
@dp.callback_query_handler(text="ovqat",state=Farms.quyon)
async def Feeding(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    quyonlar = int(about['quyon'])
    sabzilar = int(about['sabzi'])

    if sabzilar >= quyonlar:
        qoldi = sabzilar - quyonlar
        update_farm("sabzi",qoldi,user_id)
        level_quyon(user_id,3)
        await call.message.answer("✅ Ovqatlantirish muvofaqiyatli tugadi",reply_markup=qaytish)
        # await call.message.answer("👩‍🌾 Ferma bo'limi ",reply_markup=ruyxat_inline)
        await call.message.delete()
        await Farms.ovqat_tugadi.set()
    else:
        balo = await call.message.answer("❌ Sabzilar yetarli emas")
        await asyncio.sleep(5)
        await balo.delete()


@dp.callback_query_handler(text="urqa",state=Farms.ovqat_tugadi)
async def Tugabpti(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    bor = int(about['quyon']) ## 2 - element bu quyon
    sabzi = int(about['sabzi']) ## 4 - element bu sabzilar
    levl = about['lvlquyon'].split(",")[0]
    if bor >=1:
        await call.message.answer(f"🐰 <b>Sizni quyonlaringiz</b>\n✅ <b>Jami: {bor} ta</b> \
            \n🥕 Sabzilar: {sabzi} ta \n🏆 Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.quyon.set()
    else:
        await call.message.answer("❌ Sizda quyonlar yo'q")




## BItta quyoni sotish uchun code
@dp.callback_query_handler(text="sotish1",state=Farms.quyon)
async def Sotma(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    quyon = int(about['quyon'])
    lvl = about['lvlquyon'].split(",")[0]
    lvl = int(lvl)

    await call.message.delete()
    if quyon >= 1:
        if lvl < 4:
            await call.message.answer(f"1 ta quyonni sotasizmi ❓\
                \nNarxi: 149 $",reply_markup=sotaman)
            await Savdo.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"1 ta quyonni sotasizmi ❓\
                \nNarxi: 249 $",reply_markup=sotaman)
            await Savdo.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"1 ta quyonni sotasizmi ❓\
                \nNarxi: 349 $",reply_markup=sotaman)
            await Savdo.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"1 ta quyonni sotasizmi ❓\
                \nNarxi: 449 $",reply_markup=sotaman)
            await Savdo.lvl4.set()
        else:
            await call.message.answer(f"1 ta quyonni sotasizmi ❓\
                \nNarxi: 599 $",reply_markup=sotaman)
            await Savdo.lvl5.set()



@dp.callback_query_handler(text="sotish5",state=Farms.quyon)
async def soyma5(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    quyon = int(about['quyon'])
    lvl = about['lvlquyon'].split(",")[0]
    lvl = int(lvl)

    if quyon >= 5:
        if lvl < 4:
            await call.message.answer(f"5 ta quyonni sotasizmi ❓\
                \nNarxi: 749 $",reply_markup=sotaman)
            await Savdo5x.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"5 ta quyonni sotasizmi ❓\
                \nNarxi: 1249 $",reply_markup=sotaman)
            await Savdo5x.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"5 ta quyonni sotasizmi ❓\
                \nNarxi: 1749 $",reply_markup=sotaman)
            await Savdo5x.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"5 ta quyonni sotasizmi ❓\
                \nNarxi: 2249 $",reply_markup=sotaman)
            await Savdo5x.lvl4.set()
        else:
            await call.message.answer(f"5 ta quyonni sotasizmi ❓\
                \nNarxi: 2400 $",reply_markup=sotaman)
            await Savdo5x.lvl5.set()
        await call.message.delete()
    else:
        balo = await call.message.answer("Szida 5 ta quyon yo'q ‼")
        await asyncio.sleep(4)
        await balo.delete()