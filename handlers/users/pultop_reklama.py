from aiogram.types import Message,CallbackQuery,InlineQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from data.inline_query import reklama1,reklama2

from states.All_State import *
from .functions import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.pul_uvhun import *
import asyncio



@dp.message_handler(text="🛍 Reklama",state=PulTop.turlar)
async def ReklamaXizmati(ms:Message):
    await ms.answer("Tugmani bosib chat tanlang\n<b>1 ta reklama: 3 $</b>",reply_markup=rek_lama)
    await PulTop.reklama.set()


# @dp.inline_handler(text="rek")
@dp.inline_handler(text="rek",state=PulTop.reklama)
async def Reksi(query:InlineQuery,state:FSMContext):
    date = await state.get_data()
    idn = int(date.get("user_id"))
    await query.answer(results=reklama1)
    b = pullari(idn)
    update_baza("pul",b+3,idn)


# @dp.inline_handler(text="reklama")
@dp.inline_handler(text="reklama",state=PulTop.reklama)
async def Reksi(query:InlineQuery,state:FSMContext):
    date = await state.get_data()
    idn = int(date.get("user_id"))
    b = pullari(idn)
    update_baza("pul",b+3,idn)
    await query.answer(results=reklama2)


@dp.callback_query_handler(text="orqaga",state=PulTop.reklama)
async def Tuaj(call:CallbackQuery):
    await call.message.answer("Pul topish uchun quyidagi o'yinlar bor",reply_markup=pul_tanlash)
    await call.message.delete()
    await PulTop.turlar.set()



