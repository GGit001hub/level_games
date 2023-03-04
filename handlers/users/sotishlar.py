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




@dp.callback_query_handler(text="yuq",state=Savdo.all_states_names)
@dp.callback_query_handler(text="yuq",state=TVsavdo.all_states_names)
@dp.callback_query_handler(text="yuq",state=Savdo5x.all_states_names)
@dp.callback_query_handler(text="yuq",state=TVsavdo5x.all_states_names)
async def Sanma(call:CallbackQuery):
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()


## Bita quyon sotaman bosganda ishga tushadi 👇
## Bita quyon sotaman bosganda ishga tushadi  👇
## Bita quyon sotaman bosganda ishga tushadi   👇
@dp.callback_query_handler(text="ha",state=Savdo.lvl1)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    about = select_users_farm(userid)
    quyon = about[2]
    nimasi = int(quyon) - 1
    update_farm("quyon",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about[5]) + 149
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish
    lvl_about = about[6]
    lvl = lvl_about[0]
    dan = lvl_about[-1].split("/")[-1]
    buldi = lvl_about[-1].split("/")[0]
    ayridi = int(buldi) - 2
    malta = f"{lvl},{ayridi}/{dan}"
    update_farm("lvlquyon",malta,userid)



@dp.callback_query_handler(text="ha",state=Savdo.lvl2)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    about = select_users_farm(userid)
    quyon = about[2]
    nimasi = int(quyon) - 1
    update_farm("quyon",nimasi,userid)

    user_about = select_users(userid)
    kumushlar = int(user_about[5]) + 249
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish
    lvl_about = about[6]
    lvl = lvl_about[0]
    dan = lvl_about[-1].split("/")[-1]
    buldi = lvl_about[-1].split("/")[0]
    ayridi = int(buldi) - 3
    malta = f"{lvl},{ayridi}/{dan}"
    update_farm("lvlquyon",malta,userid)



@dp.callback_query_handler(text="ha",state=Savdo.lvl3)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    about = select_users_farm(userid)
    quyon = about[2]
    nimasi = int(quyon) - 1
    update_farm("quyon",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about[5]) + 349
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish
    lvl_about = about[6]
    lvl = lvl_about[0]
    dan = lvl_about[-1].split("/")[-1]
    buldi = lvl_about[-1].split("/")[0]
    ayridi = int(buldi) - 4
    malta = f"{lvl},{ayridi}/{dan}"
    update_farm("lvlquyon",malta,userid)




@dp.callback_query_handler(text="ha",state=Savdo.lvl4)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    about = select_users_farm(userid)
    quyon = about[2]
    nimasi = int(quyon) - 1
    update_farm("quyon",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about[5]) + 449
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish
    lvl_about = about[6]
    lvl = lvl_about[0]
    dan = lvl_about[-1].split("/")[-1]
    buldi = lvl_about[-1].split("/")[0]
    ayridi = int(buldi) - 4
    malta = f"{lvl},{ayridi}/{dan}"
    update_farm("lvlquyon",malta,userid)



@dp.callback_query_handler(text="ha",state=Savdo.lvl5)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    about = select_users_farm(userid)
    quyon = about[2]
    nimasi = int(quyon) - 1
    update_farm("quyon",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about[5]) + 600
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish
    lvl_about = about[6]
    lvl = lvl_about[0]
    dan = lvl_about[-1].split("/")[-1]
    buldi = lvl_about[-1].split("/")[0]
    ayridi = int(buldi) - 5
    malta = f"{lvl},{ayridi}/{dan}"
    update_farm("lvlquyon",malta,userid)



## Shu joydan pasti 5x sotish uchun 👇
## Shu joydan pasti 5x sotish uchun  👇
## Shu joydan pasti 5x sotish uchun   👇



@dp.callback_query_handler(text="ha",state=Savdo5x.lvl1)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)## quyon sotish uchun
    quyon = about[2]
    sotildi = int(quyon) - 5
    update_farm("quyon",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about[5]
    barcha_pul = int(pul) + 749
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta quyon sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon levelni kamaytirish uchun
    level_quyon(user_id,-7)



@dp.callback_query_handler(text="ha",state=Savdo5x.lvl2)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)## quyon sotish uchun
    quyon = about[2]
    sotildi = int(quyon) - 5
    update_farm("quyon",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about[5]
    barcha_pul = int(pul) + 1249
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta quyon sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon leveli kamayadi dwo
    level_quyon(user_id,-9)





@dp.callback_query_handler(text="ha",state=Savdo5x.lvl3)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)## quyon sotish uchun
    quyon = about[2]
    sotildi = int(quyon) - 5
    update_farm("quyon",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about[5]
    barcha_pul = int(pul) + 1749
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta quyon sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon leveli kamayadi 
    level_quyon(user_id,-10)





@dp.callback_query_handler(text="ha",state=Savdo5x.lvl4)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)## quyon sotish uchun
    quyon = about[2]
    sotildi = int(quyon) - 5
    update_farm("quyon",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about[5]
    barcha_pul = int(pul) + 2249
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta quyon sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon leveli kamayadi 
    level_quyon(user_id,-11)



@dp.callback_query_handler(text="ha",state=Savdo5x.lvl5)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    about = select_users_farm(user_id)## quyon sotish uchun
    quyon = about[2]
    sotildi = int(quyon) - 5
    update_farm("quyon",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about[5]
    barcha_pul = int(pul) + 2400
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta quyon sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## quyon leveli kamayadi dwo
    level_quyon(user_id,-12)

