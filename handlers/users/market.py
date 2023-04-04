from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from .functions import *
from .function_farm import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.savdo_button import *
import asyncio


@dp.message_handler(text="🛍 Xaridlar",state=Games.bosh_holat)
async def asdaet_Place(ms:Message):
    await ms.answer("Nima xarid qilasiz ❓",reply_markup=set_market)
    await Marketnig.bosh_holat.set()


@dp.callback_query_handler(text="kumush",state=Marketnig.bosh_holat)
async def KMSHxona(call:CallbackQuery):
    await call.message.answer("💎 <b>Qancha kumush xarid qilasiz</b> ❓",reply_markup=kumush_set)
    await call.message.delete()
    await Marketnig.kumushs.set()



@dp.callback_query_handler(text="pul",state=Marketnig.bosh_holat)
async def Pulxona(call:CallbackQuery):
    await call.message.answer("💰 <b>Qancha pul xarid qilasiz</b> ❓",reply_markup=pull_set)
    await call.message.delete()
    await Marketnig.pulls.set()




@dp.callback_query_handler(text="ferma",state=Marketnig.bosh_holat)
async def Pulxona(call:CallbackQuery):
    await call.message.answer("👩‍🌾 <b>Quyidagilardan tanlang </b>‼",reply_markup=set_ferma)
    await call.message.delete()
    await Marketnig.fermas.set()



## Xaridlar bo'limiga qaytish uchun handler

@dp.callback_query_handler(text="magazin",state=Marketnig.fermas)
@dp.callback_query_handler(text="magazin",state=Marketnig.kumushs)
@dp.callback_query_handler(text="magazin",state=Marketnig.pulls)
async def Magzixaon(call:CallbackQuery):
    await call.message.answer("Nima xarid qilasiz ❓",reply_markup=set_market)
    await call.message.delete()
    await Marketnig.bosh_holat.set()




@dp.callback_query_handler(text="nazat",state=Marketnig.bosh_holat)
async def Nazatxona(call:CallbackQuery):
    await call.message.answer("Bosh menyu ",reply_markup=level_games)
    await call.message.delete()
    await Games.bosh_holat.set()




@dp.callback_query_handler(text="hisob",state=Marketnig.bosh_holat)
async def Hisobxona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user_id = int(user_id)

    user_about = select_users(user_id)
    pul = int(user_about['pul'])
    kumush = int(user_about['kumush'])
    malumot = f"💰 <b>Hisobingiz</b>: {pul} $\n💎 <b>Kumushlar</b>: {kumush}"
    balo = await call.message.answer(malumot)
    await asyncio.sleep(5)
    await balo.delete()

