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
    about = select_users_farm(user_id)
    bor = about[3] ## 3 - element bu tovuq
    sabzi = about[5] ## 5 - element bu donlar
    levl = about[7].split(",")[0]
    if bor >=1:
        await call.message.answer(f"š <b>Sizni tovuqlarizgiz</b>\nā <b>Jami: {bor} ta</b> \
            \nš½ Donlar: {sabzi} ta \nš Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.tovuq.set()
    else:
        baol = await call.message.answer("Sizda tovuq yo'q")
        await asyncio.sleep(3)
        await baol.delete()



@dp.callback_query_handler(text="orqaga",state=Farms.tovuq)
async def Sidawn(call:CallbackQuery):
    await call.message.answer("š Ferma bo'limi š©āš¾",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()



## Tovuqga ovqat berish uchun code š
@dp.callback_query_handler(text="ovqat",state=Farms.tovuq)
async def Feeding(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)
    tovuqlar = about[3]
    donlar = about[5]

    if donlar >= tovuqlar:
        qoldi = donlar - tovuqlar
        update_farm("don",qoldi,user_id)
        level_tovuq(user_id,3)
        await call.message.answer("ā Ovqatlantirish muvofaqiyatli tugadi",reply_markup=qaytish)
        # await call.message.answer("š©āš¾ Ferma bo'limi ",reply_markup=ruyxat_inline)
        await call.message.delete()
        await Farms.ovqat_tgd.set()
    else:
        balo = await call.message.answer("ā Donlar yetarli emas")
        await asyncio.sleep(5)
        await balo.delete()



@dp.callback_query_handler(text="urqa",state=Farms.ovqat_tgd)
async def Tugabpti(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)
    bor = about[3] ## 2 - element bu quyon
    sabzi = about[5] ## 4 - element bu sabzilar
    levl = about[7].split(",")[0]
    if bor >=1:
        await call.message.answer(f"š <b>Sizni tovuqlaringiz</b>\nā <b>Jami: {bor} ta</b> \
            \nš½ Donlar: {sabzi} ta \nš Darajasi: {levl}",reply_markup=hal_qilish)
        await call.message.delete()
        await Farms.tovuq.set()
    else:
        await call.message.answer("ā Sizda tovuqlar yo'q")





## BItta tovuqni sotish uchun code
@dp.callback_query_handler(text="sotish1",state=Farms.tovuq)
async def Sotma(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)
    quyon = about[3]
    lvl = about[7].split(",")[0]
    lvl = int(lvl)

    await call.message.delete()
    if quyon >= 1:
        if lvl < 4:
            await call.message.answer(f"1 ta tovuqni sotasizmi ā\
                \nNarxi: 109 $",reply_markup=sotaman)
            await TVsavdo.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"1 ta tovuqni sotasizmi ā\
                \nNarxi: 219 $",reply_markup=sotaman)
            await TVsavdo.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"1 ta tovuqni sotasizmi ā\
                \nNarxi: 329 $",reply_markup=sotaman)
            await TVsavdo.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"1 ta tovuqni sotasizmi ā\
                \nNarxi: 439 $",reply_markup=sotaman)
            await TVsavdo.lvl4.set()
        else:
            await call.message.answer(f"1 ta tovuqni sotasizmi ā\
                \nNarxi: 549 $",reply_markup=sotaman)
            await TVsavdo.lvl5.set()
        await call.message.delete()



## 5 ta tovuq sotish uchun handler
@dp.callback_query_handler(text="sotish5",state=Farms.tovuq)
async def soyma5(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")

    about = select_users_farm(user_id)
    quyon = about[3]
    lvl = about[7].split(",")[0]
    lvl = int(lvl)

    if quyon >= 5:
        if lvl < 4:
            await call.message.answer(f"5 ta tovuqni sotasizmi ā\
                \nNarxi: 549 $",reply_markup=sotaman)
            await TVsavdo5x.lvl1.set()
        elif lvl < 8:
            await call.message.answer(f"5 ta tovuqni sotasizmi ā\
                \nNarxi: 1099 $",reply_markup=sotaman)
            await TVsavdo5x.lvl2.set()
        elif lvl < 12:
            await call.message.answer(f"5 ta tovuqni sotasizmi ā\
                \nNarxi: 1649 $",reply_markup=sotaman)
            await TVsavdo5x.lvl3.set()
        elif lvl < 15 :
            await call.message.answer(f"5 ta tovuqni sotasizmi ā\
                \nNarxi: 2199 $",reply_markup=sotaman)
            await TVsavdo5x.lvl4.set()
        else:
            await call.message.answer(f"5 ta tovuqni sotasizmi ā\
                \nNarxi: 2299 $",reply_markup=sotaman)
            await TVsavdo5x.lvl5.set()
        await call.message.delete()
    
    else:
        balo = await call.message.answer("Sizda 5 ta tovuq yo'q ā¼")
        await asyncio.sleep(4)
        await balo.delete()
