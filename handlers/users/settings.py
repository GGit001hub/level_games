from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from .functions import *
from states.All_State import *
from keyboards.default.for_start import *
from keyboards.inline.sozlamalar import *

import asyncio



@dp.message_handler(text="⚙️ Sozlamalar",state=Games.all_states_names)
async def SettinGS(ms:Message):
    xabar = "Qanday o'zgartirish kiritasiz 🔄"
    await ms.answer(xabar,reply_markup=settings)
    await Nastroyka.tanlash.set()


## Ism almashtirish uchun
## Ism almashtirish uchun
@dp.callback_query_handler(text="name_change",state=Nastroyka.tanlash)
async def NameSet(call:CallbackQuery):
    await call.message.answer("Yangi <b>ismni</b> kiritng ‼")
    await Nastroyka.name_set.set()
    await call.message.delete()

@dp.message_handler(state=Nastroyka.name_set)
async def Qaundas(ms:Message,state:FSMContext):
    date = await state.get_data()
    info = date.get("user_id")
    yangi_ism = ms.text
    update_baza('name',f"{yangi_ism}",info)
    await ms.answer("Qanday o'zgartirish kiritasiz 🔄",reply_markup=settings)
    await Nastroyka.tanlash.set()



@dp.callback_query_handler(text="password",state=Nastroyka.tanlash)
async def PassWord(call:CallbackQuery):
    balo = await call.message.answer("Parolni yangilash uchun avval eski parolni kiriting ❗")
    await call.message.delete()
    await Nastroyka.eski_parol.set()
    await asyncio.sleep(15)
    await balo.delete()



@dp.message_handler(state=Nastroyka.eski_parol)
async def Eski(ms:Message,state:FSMContext):
    date = await state.get_data()
    info = date.get("user_id")
    eski_parol = ms.text
    user = select_users(info)
    parol = user[3]
    if eski_parol == parol:
        await ms.answer("Yangi parolni kiriting")
        await Nastroyka.password_set.set()
    else:
        await ms.answer("Kechirasiz bu parol xato")
    await ms.delete()


@dp.message_handler(state=Nastroyka.password_set)
async def japjd(ms:Message,state:FSMContext):
    date = await state.get_data()
    info = date.get("user_id")
    parl = ms.text
    update_baza('parol',parl,info)
    await ms.answer("✅ Parol o'zgartirildi",reply_markup=settings)
    await Nastroyka.tanlash.set()
    
    await ms.delete()
    # await asyncio.sleep(5)
    # await balo.delete()


@dp.callback_query_handler(text="orqaga",state=Nastroyka.tanlash)
async def OrqaGa(call:CallbackQuery):
    await call.message.answer("Bosh sahifa",reply_markup=level_games)
    await call.message.delete()
    await Games.bosh_holat.set()




@dp.callback_query_handler(text="loguot",state=Nastroyka.tanlash)
async def Vixot(call:CallbackQuery):
    await call.message.answer("Rostanham chiqasizmi ❓",reply_markup=chiqasizmi)
    await call.message.delete()
    await Nastroyka.logout.set()


@dp.callback_query_handler(text="yes",state=Nastroyka.logout)
async def Chiqdim(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Accountga kiring ‼\nYoki ro'yxatdan o'ting",reply_markup=login)
    await call.message.delete()
    await Register.bosh_holat.set()


@dp.callback_query_handler(text="net",state=Nastroyka.logout)
async def NotVhi(call:CallbackQuery):
    xabar = "Qanday o'zgartirish kiritasiz 🔄"
    await call.message.answer(xabar,reply_markup=settings)
    await Nastroyka.tanlash.set()
