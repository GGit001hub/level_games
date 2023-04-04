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


@dp.callback_query_handler(text="chicken",state=Farms.bosh_holat)
async def Quyon_xona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    bor = int(about['tovuq']) ## 3 - element bu tovuq
    sabzi = int(about['don']) ## 5 - element bu donlar
    levl = about['lvltovuq'].split(",")[0]
    if bor >=1:
        await call.message.answer(f"🐓 <b>Sizni tovuqlarizgiz</b>\n✅ <b>Jami: {bor} ta</b> \
            \n🌽 Donlar: {sabzi} ta \n🏆 Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.tovuq.set()
    else:
        baol = await call.message.answer("Sizda tovuq yo'q")
        await asyncio.sleep(3)
        await baol.delete()



@dp.callback_query_handler(text="orqaga",state=Farms.tovuq)
async def Sidawn(call:CallbackQuery):
    await call.message.answer("👉 Ferma bo'limi 👩‍🌾",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()



## Tovuqga ovqat berish uchun code 👇
@dp.callback_query_handler(text="ovqat",state=Farms.tovuq)
async def Feeding(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    tovuqlar = int(about['tovuq'])
    donlar = int(about['don'])

    if donlar >= tovuqlar:
        qoldi = donlar - tovuqlar
        update_farm("don",qoldi,user_id)
        level_tovuq(user_id,3)
        await call.message.answer("✅ Ovqatlantirish muvofaqiyatli tugadi",reply_markup=qaytish)
        # await call.message.answer("👩‍🌾 Ferma bo'limi ",reply_markup=ruyxat_inline)
        await call.message.delete()
        await Farms.ovqat_tgd.set()
    else:
        balo = await call.message.answer("❌ Donlar yetarli emas")
        await asyncio.sleep(5)
        await balo.delete()



@dp.callback_query_handler(text="urqa",state=Farms.ovqat_tgd)
async def Tugabpti(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    bor = int(about['tovuq']) ## 2 - element bu quyon
    sabzi = int(about['don']) ## 4 - element bu sabzilar
    levl = about['lvltovuq'].split(",")[0]
    if bor >=1:
        await call.message.answer(f"🐓 <b>Sizni tovuqlaringiz</b>\n✅ <b>Jami: {bor} ta</b> \
            \n🌽 Donlar: {sabzi} ta \n🏆 Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.tovuq.set()
    else:
        await call.message.answer("❌ Sizda tovuqlar yo'q")





## BItta tovuqni sotish uchun code
@dp.callback_query_handler(text="sotish1",state=Farms.tovuq)
async def Sotma(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)
    quyon = int(about['quyon'])
    lvl = about['lvlquyon'].split(",")[0]
    lvl = int(lvl)

    # await call.message.delete()
    if quyon >= 1:
        if lvl < 4:
            await call.message.answer(f"1 ta tovuqni sotasizmi ❓\
                \nNarxi: 109 $",reply_markup=sotaman)
            await TVsavdo.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"1 ta tovuqni sotasizmi ❓\
                \nNarxi: 219 $",reply_markup=sotaman)
            await TVsavdo.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"1 ta tovuqni sotasizmi ❓\
                \nNarxi: 329 $",reply_markup=sotaman)
            await TVsavdo.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"1 ta tovuqni sotasizmi ❓\
                \nNarxi: 439 $",reply_markup=sotaman)
            await TVsavdo.lvl4.set()
        else:
            await call.message.answer(f"1 ta tovuqni sotasizmi ❓\
                \nNarxi: 549 $",reply_markup=sotaman)
            await TVsavdo.lvl5.set()
        await call.message.delete()



## 5 ta tovuq sotish uchun handler
@dp.callback_query_handler(text="sotish5",state=Farms.tovuq)
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
            await call.message.answer(f"5 ta tovuqni sotasizmi ❓\
                \nNarxi: 549 $",reply_markup=sotaman)
            await TVsavdo5x.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"5 ta tovuqni sotasizmi ❓\
                \nNarxi: 1099 $",reply_markup=sotaman)
            await TVsavdo5x.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"5 ta tovuqni sotasizmi ❓\
                \nNarxi: 1649 $",reply_markup=sotaman)
            await TVsavdo5x.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"5 ta tovuqni sotasizmi ❓\
                \nNarxi: 2199 $",reply_markup=sotaman)
            await TVsavdo5x.lvl4.set()
        else:
            await call.message.answer(f"5 ta tovuqni sotasizmi ❓\
                \nNarxi: 2299 $",reply_markup=sotaman)
            await TVsavdo5x.lvl5.set()
        await call.message.delete()
    
    else:
        balo = await call.message.answer("Sizda 5 ta tovuq yo'q ‼")
        await asyncio.sleep(4)
        await balo.delete()
