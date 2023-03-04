from aiogram.types import Message,CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext

from states.All_State import *
from .functions import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.pul_uvhun import *

import random
import asyncio


@dp.callback_query_handler(text="orqaga",state=PulTop.besh_tikish)
@dp.callback_query_handler(text="orqaga",state=PulTop.onbesh_tikish)
@dp.callback_query_handler(text="orqaga",state=PulTop.yigirma_tikish)
@dp.callback_query_handler(text="orqaga",state=PulTop.on_tikish)
@dp.callback_query_handler(text="orqaga",state=PulTop.ellik_tikish)
async def Natr(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    xabar = "Qancha pul tikasiz. Tanlang"
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()
    await call.message.delete()




@dp.callback_query_handler(text="birga",state=PulTop.besh_tikish)
async def BeshTikdi(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idsi = date.get("user_id")
    user_puli = pullari(idsi)
    minus = user_puli - 5

    tasodif = random.randint(1,10)
    hisob = minus + tasodif
    update_baza('pul',hisob,idsi)
    await call.message.delete()

    await asyncio.sleep(2)
    xabar = f"🎉 Siz tanlagan raqam ortida \
        \n<b>{tasodif} $</b>yashiringan edi ✅\n<b>Yana pul tikasizmi</b> ❓"  
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()



@dp.callback_query_handler(text="birga",state=PulTop.on_tikish)
async def BeshTikdi(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idsi = date.get("user_id")
    user_puli = pullari(idsi)
    minus = user_puli - 10

    tasodif = random.randint(1,16)
    hisob = minus + tasodif
    update_baza('pul',hisob,idsi)
    await call.message.delete()

    await asyncio.sleep(2)
    xabar = f"🎉 Siz tanlagan raqam ortida \
        \n<b>{tasodif} $</b>yashiringan edi ✅\n<b>Yana pul tikasizmi</b> ❓"
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()




@dp.callback_query_handler(text="birga",state=PulTop.onbesh_tikish)
async def BeshTikdi(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idsi = date.get("user_id")
    user_puli = pullari(idsi)
    minus = user_puli - 15

    tasodif = random.randint(1,25)
    hisob = minus + tasodif
    update_baza('pul',hisob,idsi)
    await call.message.delete()

    await asyncio.sleep(2)
    xabar = f"🎉 Siz tanlagan raqam ortida \
        \n<b>{tasodif} $</b>yashiringan edi ✅\n<b>Yana pul tikasizmi</b> ❓"  
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()




@dp.callback_query_handler(text="birga",state=PulTop.yigirma_tikish)
async def BeshTikdi(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idsi = date.get("user_id")
    user_puli = pullari(idsi)
    minus = user_puli - 20

    tasodif = random.randint(1,40)
    hisob = minus + tasodif
    update_baza('pul',hisob,idsi)
    await call.message.delete()

    await asyncio.sleep(2)
    xabar = f"🎉 Siz tanlagan raqam ortida \
        \n<b>{tasodif} $ </b>yashiringan edi ✅\n<b>Yana pul tikasizmi</b> ❓"  
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()





@dp.callback_query_handler(text="birga",state=PulTop.ellik_tikish)
async def BeshTikdi(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idsi = date.get("user_id")
    user_puli = pullari(idsi)
    minus = user_puli - 50

    tasodif = random.randint(1,70)
    hisob = minus + tasodif
    update_baza('pul',hisob,idsi)
    await call.message.delete()

    await asyncio.sleep(2)
    xabar = f"🎉 Siz tanlagan raqam ortida \
        \n<b>{tasodif} $</b>yashiringan edi ✅\n<b>Yana pul tikasizmi</b> ❓"
    await call.message.answer(xabar,reply_markup=tikish)
    await PulTop.tikish.set()
