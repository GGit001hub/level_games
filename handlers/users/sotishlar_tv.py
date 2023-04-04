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






## Bita tovuq sotaman bosganda ishga tushadi 👇
## Bita tovuq sotaman bosganda ishga tushadi  👇
## Bita tovuq sotaman bosganda ishga tushadi   👇
@dp.callback_query_handler(text="ha",state=TVsavdo.lvl1)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    userid = int(userid)
    about = select_users_farm(userid)
    quyon = about['tovuq']
    nimasi = int(quyon) - 1
    update_farm("tovuq",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about['kumush']) + 109
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(userid,-2)


@dp.callback_query_handler(text="ha",state=TVsavdo.lvl2)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    userid = int(userid)
    about = select_users_farm(userid)
    quyon = about['tovuq']
    nimasi = int(quyon) - 1
    update_farm("tovuq",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about['kumush']) + 219
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(userid,-3)


@dp.callback_query_handler(text="ha",state=TVsavdo.lvl3)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    userid = int(userid)
    about = select_users_farm(userid)
    quyon = about['tovuq']
    nimasi = int(quyon) - 1
    update_farm("tovuq",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about['kumush']) + 329
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(userid,-4)


@dp.callback_query_handler(text="ha",state=TVsavdo.lvl4)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    userid = int(userid)
    about = select_users_farm(userid)
    quyon = about['tovuq']
    nimasi = int(quyon) - 1
    update_farm("tovuq",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about['kumush']) + 439
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(userid,-5)


@dp.callback_query_handler(text="ha",state=TVsavdo.lvl5)
async def Levl1(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get("user_id")
    userid = int(userid)
    about = select_users_farm(userid)
    quyon = about['tovuq']
    nimasi = int(quyon) - 1
    update_farm("tovuq",nimasi,userid)
    user_about = select_users(userid)
    kumushlar = int(user_about['kumush']) + 549
    update_baza("pul",kumushlar,userid)
    await call.message.answer("👩‍🌾 Ferma bo'limi",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(userid,-5)




## Shu joydan pasti 5x sotish uchun 👇
## Shu joydan pasti 5x sotish uchun  👇
## Shu joydan pasti 5x sotish uchun   👇


@dp.callback_query_handler(text="ha",state=TVsavdo5x.lvl1)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)## tovuq sotish uchun
    quyon = about['tovuq']
    sotildi = int(quyon) - 5
    update_farm("tovuq",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about['pul']
    barcha_pul = int(pul) + 549
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta tovuq sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(user_id,-7)



@dp.callback_query_handler(text="ha",state=TVsavdo5x.lvl2)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)## tovuq sotish uchun
    quyon = about['tovuq']
    sotildi = int(quyon) - 5
    update_farm("tovuq",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about['pul']
    barcha_pul = int(pul) + 1099
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta tovuq sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(user_id,-9)


@dp.callback_query_handler(text="ha",state=TVsavdo5x.lvl3)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)## tovuq sotish uchun
    quyon = about['tovuq']
    sotildi = int(quyon) - 5
    update_farm("tovuq",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about['pul']
    barcha_pul = int(pul) + 1649
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta tovuq sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(user_id,-13)



@dp.callback_query_handler(text="ha",state=TVsavdo5x.lvl4)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)## tovuq sotish uchun
    quyon = about['tovuq']
    sotildi = int(quyon) - 5
    update_farm("tovuq",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about['pul']
    barcha_pul = int(pul) + 2199
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta tovuq sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(user_id,-15)



@dp.callback_query_handler(text="ha",state=TVsavdo5x.lvl5)
async def listen5x(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)
    about = select_users_farm(user_id)## tovuq sotish uchun
    quyon = about['tovuq']
    sotildi = int(quyon) - 5
    update_farm("tovuq",sotildi,user_id)

    user_about = select_users(user_id) ## Sotgani uchun pul qo'shiladi
    pul = user_about['pul']
    barcha_pul = int(pul) + 2299
    update_baza("pul",barcha_pul,user_id)
    await call.message.answer("👩‍🌾 Ferma bo'limi. 5 ta tovuq sotildi ✅",reply_markup=ruyxat_inline)
    await call.message.delete()
    await Farms.bosh_holat.set()
    ## tovuq darajasini tushurish uchun
    level_tovuq(user_id,-16)

